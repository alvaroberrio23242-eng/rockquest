from app import db


class Grammy(db.Model):
    __tablename__ = 'grammys'

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(150), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    ganador = db.Column(db.String(150), nullable=False)
    obra = db.Column(db.String(200))
    descripcion = db.Column(db.Text)
    imagen_url = db.Column(db.String(300))

    def __repr__(self):
        return f'<Grammy {self.anio} {self.categoria} — {self.ganador}>'
