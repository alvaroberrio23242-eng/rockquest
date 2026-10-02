import os

from app import create_app

app = create_app()

if __name__ == '__main__':
    # El modo debug NUNCA va hardcodeado en True: se controla con la
    # variable de entorno FLASK_DEBUG y arranca apagado por defecto.
    debug = os.environ.get('FLASK_DEBUG', '').lower() in ('1', 'true', 'si')
    app.run(debug=debug)
