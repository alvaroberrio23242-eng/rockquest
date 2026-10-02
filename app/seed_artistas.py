from app import create_app, db
from app.models.artista import Artista

app = create_app()

artistas_iniciales = [
    Artista(nombre="John Lennon", instrumento_principal="Voz, Guitarra", banda_principal="The Beatles",
            pais="Reino Unido", anio_nacimiento=1940, anio_fallecimiento=1980,
            biografia="Co-fundador de The Beatles junto a Paul McCartney. Su carrera solista y su activismo "
                       "por la paz lo convirtieron en una de las figuras más influyentes de la cultura del "
                       "siglo XX."),
    Artista(nombre="Robert Plant", instrumento_principal="Voz", banda_principal="Led Zeppelin",
            pais="Reino Unido", anio_nacimiento=1948, anio_fallecimiento=None,
            biografia="Vocalista de Led Zeppelin, reconocido por su registro vocal excepcional y su rol clave "
                       "en definir el sonido del hard rock y el heavy metal de los 70."),
    Artista(nombre="David Gilmour", instrumento_principal="Guitarra, Voz", banda_principal="Pink Floyd",
            pais="Reino Unido", anio_nacimiento=1946, anio_fallecimiento=None,
            biografia="Guitarrista y vocalista de Pink Floyd desde 1968. Sus solos atmosféricos y su uso del "
                       "sustain definieron buena parte de la identidad sonora del rock progresivo."),
    Artista(nombre="Freddie Mercury", instrumento_principal="Voz, Piano", banda_principal="Queen",
            pais="Reino Unido", anio_nacimiento=1946, anio_fallecimiento=1991,
            biografia="Vocalista y compositor de Queen, célebre por su rango vocal de casi cuatro octavas y "
                       "su presencia escénica teatral, que redefinió lo que podía ser un show de rock en vivo."),
    Artista(nombre="Kurt Cobain", instrumento_principal="Voz, Guitarra", banda_principal="Nirvana",
            pais="Estados Unidos", anio_nacimiento=1967, anio_fallecimiento=1994,
            biografia="Líder de Nirvana y una de las figuras centrales del grunge. Su forma de escribir "
                       "canciones, cruda y directa, cambió el rumbo del rock alternativo de los 90."),
]

with app.app_context():
    if Artista.query.count() == 0:
        db.session.bulk_save_objects(artistas_iniciales)
        db.session.commit()
        print(f"{len(artistas_iniciales)} artistas insertados correctamente.")
    else:
        print("La tabla de artistas ya tiene datos, no se volvio a sembrar.")