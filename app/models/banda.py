from app import db


class Banda(db.Model):
    __tablename__ = 'bandas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100))
    pais = db.Column(db.String(100))
    anio_formacion = db.Column(db.Integer)
    anio_disolucion = db.Column(db.Integer, nullable=True)
    decada_principal = db.Column(db.String(10))
    biografia = db.Column(db.Text)
    imagen_url = db.Column(db.String(300))

    popularidad = db.Column(db.Integer, default=0)
    grammys_totales = db.Column(db.Integer, default=0)
    ventas_estimadas = db.Column(db.BigInteger, default=0)
    indice_influencia = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Banda {self.nombre}>'
