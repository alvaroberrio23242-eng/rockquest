from app import db


class Record(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    poseedor = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(100))
    valor = db.Column(db.String(100))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.Text)
    imagen_url = db.Column(db.String(300))

    def __repr__(self):
        return f'<Record {self.titulo} — {self.poseedor}>'
