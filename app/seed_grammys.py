from app import create_app, db
from app.models.grammy import Grammy
from app.services.utils import imagen_generica

app = create_app()

grammys_iniciales = [
    Grammy(categoria="Grammy Lifetime Achievement Award", anio=1972, ganador="The Beatles",
           obra="Trayectoria completa",
           descripcion="Reconocimiento a la trayectoria e influencia de la banda en la música popular.",
           imagen_url=imagen_generica("grammys", 0)),
    Grammy(categoria="Best Rock Performance by a Duo or Group", anio=1970, ganador="Led Zeppelin",
           obra="Led Zeppelin II (nominación histórica)",
           descripcion="Una de las nominaciones que consolidó a la banda como pionera del hard rock.",
           imagen_url=imagen_generica("grammys", 1)),
    Grammy(categoria="Best Rock Album", anio=1994, ganador="Nirvana",
           obra="MTV Unplugged in New York",
           descripcion="Grammy póstumo por el álbum acústico grabado en 1993.",
           imagen_url=imagen_generica("grammys", 2)),
    Grammy(categoria="Grammy Hall of Fame", anio=1998, ganador="Pink Floyd",
           obra="The Dark Side of the Moon",
           descripcion="Incluido en el Hall of Fame por su impacto duradero en la música.",
           imagen_url=imagen_generica("grammys", 3)),
    Grammy(categoria="Best Rock Performance by a Duo or Group", anio=1981, ganador="Queen",
           obra="Flash Gordon (nominación)",
           descripcion="Reconocimiento a la banda liderada por Freddie Mercury.",
           imagen_url=imagen_generica("grammys", 4)),
]

with app.app_context():
    db.session.bulk_save_objects(grammys_iniciales)
    db.session.commit()
    print(f"{len(grammys_iniciales)} premios Grammy insertados correctamente.")