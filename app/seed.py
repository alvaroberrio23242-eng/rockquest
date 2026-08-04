from app import create_app, db
from app.models.banda import Banda
from app.services.utils import imagen_generica

app = create_app()

bandas_iniciales = [
    Banda(nombre="The Beatles", genero="Rock, Pop Rock", pais="Reino Unido",
          anio_formacion=1960, anio_disolucion=1970, decada_principal="1960s",
          biografia="Banda británica considerada la más influyente de la historia del rock.",
          popularidad=100, grammys_totales=7, ventas_estimadas=600000000, indice_influencia=100,
          imagen_url=imagen_generica("bandas", 0)),
    Banda(nombre="Led Zeppelin", genero="Hard Rock, Blues Rock", pais="Reino Unido",
          anio_formacion=1968, anio_disolucion=1980, decada_principal="1970s",
          biografia="Pioneros del hard rock y el heavy metal.",
          popularidad=95, grammys_totales=0, ventas_estimadas=300000000, indice_influencia=98,
          imagen_url=imagen_generica("bandas", 1)),
    Banda(nombre="Pink Floyd", genero="Rock Progresivo", pais="Reino Unido",
          anio_formacion=1965, anio_disolucion=2014, decada_principal="1970s",
          biografia="Referentes del rock progresivo y conceptual.",
          popularidad=93, grammys_totales=1, ventas_estimadas=250000000, indice_influencia=97,
          imagen_url=imagen_generica("bandas", 2)),
    Banda(nombre="Queen", genero="Rock, Glam Rock", pais="Reino Unido",
          anio_formacion=1970, anio_disolucion=None, decada_principal="1970s",
          biografia="Banda liderada por Freddie Mercury, íconos del rock teatral.",
          popularidad=98, grammys_totales=0, ventas_estimadas=300000000, indice_influencia=96,
          imagen_url=imagen_generica("bandas", 3)),
    Banda(nombre="Nirvana", genero="Grunge", pais="Estados Unidos",
          anio_formacion=1987, anio_disolucion=1994, decada_principal="1990s",
          biografia="Banda que popularizó el grunge y definió el rock alternativo de los 90.",
          popularidad=90, grammys_totales=1, ventas_estimadas=75000000, indice_influencia=94,
          imagen_url=imagen_generica("bandas", 4)),
]

with app.app_context():
    db.session.bulk_save_objects(bandas_iniciales)
    db.session.commit()
    print(f"{len(bandas_iniciales)} bandas insertadas correctamente.")