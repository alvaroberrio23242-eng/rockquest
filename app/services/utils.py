import re
import unicodedata


def slugify(texto: str) -> str:
    """
    Convierte un nombre (ej. "The Beatles") en un slug apto para
    nombre de archivo / URL (ej. "the-beatles").

    Se usa para que la ruta de imagen de cada banda/artista/premio
    sea predecible: /static/images/<categoria>/<slug>.jpg
    """
    if not texto:
        return ""
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    texto = texto.lower().strip()
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    texto = re.sub(r"-+", "-", texto).strip("-")
    return texto


def imagen_url(categoria: str, nombre: str, extension: str = "jpg") -> str:
    """
    Genera la ruta esperada de imagen local para un item.
    categoria: 'bandas' | 'artistas' | 'grammys' | 'records'
    """
    slug = slugify(nombre)
    return f"/static/images/{categoria}/{slug}.{extension}"


# ==========================================
# Imágenes genéricas de tema rock (Unsplash License: uso comercial
# libre, sin atribución requerida — https://unsplash.com/license).
# Se usan como PLACEHOLDER en vez de fotos reales de bandas/artistas o
# arte de tapa de discos: esas SI tienen derechos de autor (son fotos
# de personas identificables y portadas de álbumes), no hay version
# libre de uso de una foto de Freddie Mercury o de la tapa de
# "Nevermind", asi que no se pueden descargar/subir a un repo publico.
# En vez de dejar 404s (imagen_url() de arriba genera una ruta local
# que nadie coloco todavia), estas imagenes tematicas decorativas
# (guitarra, vinilo, escenario, microfono) evitan el error y quedan
# prolijas mientras no se agregue una foto real con licencia propia.
# ==========================================
IMAGENES_GENERICAS = {
    "bandas": [
        "https://images.unsplash.com/photo-1589131626349-2799f057b43a?w=500",  # guitarra eléctrica
        "https://images.unsplash.com/photo-1767289394567-b5e4b5986c88?w=500",  # escenario de concierto
    ],
    "artistas": [
        "https://images.unsplash.com/photo-1675430428298-ecd1827c18fd?w=500",  # micrófono
        "https://images.unsplash.com/photo-1589131626349-2799f057b43a?w=500",  # guitarra eléctrica
    ],
    "grammys": [
        "https://images.unsplash.com/photo-1645523906738-eb84e7010695?w=500",  # vinilo
        "https://images.unsplash.com/photo-1767289394567-b5e4b5986c88?w=500",  # escenario de concierto
    ],
    "records": [
        "https://images.unsplash.com/photo-1767289394567-b5e4b5986c88?w=500",  # escenario de concierto
        "https://images.unsplash.com/photo-1645523906738-eb84e7010695?w=500",  # vinilo
    ],
}


def imagen_generica(categoria: str, indice: int = 0) -> str:
    """
    Devuelve una imagen decorativa de tema rock (no una foto real de
    la banda/artista/disco especifico) para usar en 'imagen_url' de
    cada item del seed. 'indice' rota entre las opciones disponibles
    para que no todas las tarjetas de una misma categoria se vean
    con la misma foto.
    """
    opciones = IMAGENES_GENERICAS.get(categoria, IMAGENES_GENERICAS["bandas"])
    return opciones[indice % len(opciones)]