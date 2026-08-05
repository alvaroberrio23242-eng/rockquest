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
