import os

from app.services.utils import slugify

EXTENSIONES_PROBADAS = (".jpg", ".jpeg", ".png", ".webp")

# app/static/images
_CARPETA_STATIC_IMAGES = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "static", "images"
)


def imagen_local(nombre: str, categoria: str):
    """
    Busca en app/static/images/<categoria>/ un archivo cuyo nombre sea
    el slug de 'nombre' con alguna de las extensiones soportadas
    (mismo criterio que usa sync_a_rockquest.py de OSINT Search Pro
    al copiar las descargas).

    Devuelve la ruta relativa a pasarle a url_for('static', filename=...)
    si el archivo existe, o None si todavía no se sincronizó ninguna
    imagen para ese nombre (para que el template pueda mostrar un
    placeholder en vez de un <img> roto).
    """
    if not nombre:
        return None

    slug = slugify(nombre)
    carpeta = os.path.join(_CARPETA_STATIC_IMAGES, categoria)

    for extension in EXTENSIONES_PROBADAS:
        ruta_absoluta = os.path.join(carpeta, f"{slug}{extension}")
        if os.path.isfile(ruta_absoluta):
            return f"images/{categoria}/{slug}{extension}"

    return None
