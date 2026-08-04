from app import create_app, db
from app.models.record import Record
from app.services.utils import imagen_generica

app = create_app()

records_iniciales = [
    Record(titulo="Álbum más vendido de la historia", poseedor="The Beatles",
           categoria="Ventas", valor="600 millones de copias estimadas", anio=1970,
           descripcion="Suma histórica de ventas del catálogo completo de la banda.",
           imagen_url=imagen_generica("records", 0)),
    Record(titulo="Show en vivo más visto por TV (Live Aid)", poseedor="Queen",
           categoria="Presentación en vivo", valor="~1.9 mil millones de espectadores", anio=1985,
           descripcion="La actuación de Queen en Live Aid es considerada una de las mejores en vivo de la historia.",
           imagen_url=imagen_generica("records", 1)),
    Record(titulo="Álbum de rock progresivo más longevo en charts", poseedor="Pink Floyd",
           categoria="Permanencia en charts", valor="741 semanas en Billboard 200", anio=1973,
           descripcion="The Dark Side of the Moon estuvo en las listas de Billboard durante más de 14 años.",
           imagen_url=imagen_generica("records", 2)),
    Record(titulo="Álbum debut más vendido del grunge", poseedor="Nirvana",
           categoria="Ventas", valor="+30 millones de copias (Nevermind)", anio=1991,
           descripcion="Nevermind popularizó el grunge a nivel mundial y llevó a Nirvana al mainstream.",
           imagen_url=imagen_generica("records", 3)),
    Record(titulo="Gira más larga de un grupo de hard rock", poseedor="Led Zeppelin",
           categoria="Giras", valor="Más de una década de giras activas", anio=1980,
           descripcion="Una de las bandas con mayor actividad de giras entre 1968 y 1980.",
           imagen_url=imagen_generica("records", 4)),
]

with app.app_context():
    db.session.bulk_save_objects(records_iniciales)
    db.session.commit()
    print(f"{len(records_iniciales)} récords insertados correctamente.")