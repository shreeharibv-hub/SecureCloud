from flask import Flask, jsonify, request
import sqlite3
from app.database import get_db_connection, init_db
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# Health check API
@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "project": "secureCloud"
    })


# User registration API
@app.route("/api/users", methods=["POST"])
def registration():

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Data cannot be fetched"}), 400

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON format"}), 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    if "@" not in email:
        return jsonify({"error": "Invalid email"}), 400

    if len(password) < 8:
        return jsonify({
            "error": "Password length should be at least 8"
        }), 400
    hashed_password = generate_password_hash(password)
    conn = get_db_connection()
    try:
        conn.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, hashed_password)
    )
        conn.commit()
        
    except sqlite3.IntegrityError:
        return jsonify({"error":"email already exist"}),409
    finally:
        conn.close()

    return jsonify({"message": "User registered successfully"}), 201


@app.route("/api/users", methods=["GET"])
def get_users():
    conn=get_db_connection()
    users=conn.execute(
        
        "SELECT id,username,email FROM users"
    ).fetchall()
    conn.close()
    return jsonify({"users": users}), 200
# Start application
if __name__ == "__main__":
    init_db()
    app.run()