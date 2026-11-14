from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.config import DevelopmentConfig
    app.config.from_object(DevelopmentConfig)

    from app.routes.users import users_bp
    app.register_blueprint(users_bp)

    from app.routes.health import health_bp
    app.register_blueprint(health_bp)

    return app