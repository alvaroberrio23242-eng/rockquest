import os
import re
import unicodedata


def slugify(texto: str) -> str:
    """
    Convierte un nombre (ej. "The Beatles") en un slug para nombre de
    archivo (ej. "the-beatles"). Coincide con la lógica usada en
    OSINT Search Pro (services/utils.py) para que los archivos que
    ese proyecto descarga y copia a static/images/<categoria>/
    encajen directamente con lo que buscamos acá.
    """
    if not texto:
        return ""
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    texto = texto.lower().strip()
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    texto = re.sub(r"-+", "-", texto).strip("-")
    return texto


# app/static/images (misma carpeta que usa imagenes.py)
_CARPETA_STATIC_IMAGES = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "static", "images"
)

_EXTENSIONES_IMAGEN = (".jpg", ".jpeg", ".png", ".webp")


def imagen_generica(categoria: str, indice: int = 0) -> str:
    """
    Imagen generica para los seeds de grammys/records. Busca en
    static/images/<categoria>/ un archivo generica-<indice> con alguna
    extension soportada; si todavia no hay fotos cargadas devuelve el
    placeholder compartido. Los templates ademas tienen fallback
    propio via onerror, asi que nunca queda un <img> roto.
    """
    slug = f"generica-{indice}"
    carpeta = os.path.join(_CARPETA_STATIC_IMAGES, categoria)
    for extension in _EXTENSIONES_IMAGEN:
        if os.path.isfile(os.path.join(carpeta, f"{slug}{extension}")):
            return f"images/{categoria}/{slug}{extension}"
    return "images/placeholder.svg"
