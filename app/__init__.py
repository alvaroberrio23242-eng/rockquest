from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-cambiar-en-produccion'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rockquest.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.services.imagenes import imagen_local
    app.jinja_env.globals['imagen_local'] = imagen_local

    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        from app.models import banda
        from app.models import artista
        db.create_all()

    return app
