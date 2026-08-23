import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # La clave de sesiones NUNCA se hardcodea: sin SECRET_KEY en el
    # entorno la app se niega a arrancar (fail-fast).
    secret_key = os.environ.get('SECRET_KEY')
    if not secret_key:
        raise RuntimeError(
            "SECRET_KEY no esta configurada. Definela como variable de "
            "entorno antes de arrancar la aplicacion."
        )
    app.config['SECRET_KEY'] = secret_key
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
