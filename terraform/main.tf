terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

# AWS Provider
provider "aws" {
  region = var.aws_region
}

# EC2 Instance
resource "aws_instance" "securecloud_server" {
  ami                  = "ami-04b0b8ee9ce90920a"
  instance_type        = "t3.micro"
  iam_instance_profile = aws_iam_instance_profile.ssm_profile.name

  # Public IP
  associate_public_ip_address = true

  # Attach Security Group
  vpc_security_group_ids = [
    aws_security_group.securecloud-sg.id
  ]

  # Root Storage
  root_block_device {
    volume_size = 8
    volume_type = "gp3"
    encrypted   = true
  }

  # Install Docker during EC2 startup
  user_data = <<-EOF
    #!/bin/bash
    dnf update -y
    dnf install -y docker
    systemctl enable docker
    systemctl start docker
  EOF

  tags = {
    Name        = "SecureCloud-Server"
    Environment = "Development"
    Project     = "SecureCloud"
  }
}

# Security Group
resource "aws_security_group" "securecloud-sg" {
  name        = "securecloud-security-group"
  description = "Security group for SecureCloud EC2"

  # Allow HTTP traffic
  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "SecureCloud-SG"
    Project = "SecureCloud"
  }

}
resource "aws_iam_role" "ssm_role" {
  name = "securecloud-ec2-ssm-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ssm_policy" {
  role       = aws_iam_role.ssm_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

resource "aws_iam_instance_profile" "ssm_profile" {
  name = "securecloud-ec2-ssm-profile"
  role = aws_iam_role.ssm_role.name
}