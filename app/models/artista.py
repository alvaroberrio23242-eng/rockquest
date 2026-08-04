from app import db


class Artista(db.Model):
    __tablename__ = 'artistas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    instrumento_principal = db.Column(db.String(100))
    banda_principal = db.Column(db.String(100))
    pais = db.Column(db.String(100))
    anio_nacimiento = db.Column(db.Integer)
    anio_fallecimiento = db.Column(db.Integer, nullable=True)
    biografia = db.Column(db.Text)
    imagen_url = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f'<Artista {self.nombre}>'
