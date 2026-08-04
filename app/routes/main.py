from flask import Blueprint, render_template, request
from app.models.banda import Banda
from app.models.artista import Artista
from app.models.decadas_data import DECADAS
from app.models.linea_tiempo_data import HITOS
from app.models.subgeneros_data import SUBGENEROS
from app.models.trivia_data import PREGUNTAS

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/historia')
def historia():
    return render_template('historia.html')


@main_bp.route('/linea-del-tiempo')
def linea_del_tiempo():
    return render_template('linea_del_tiempo.html', hitos=HITOS)


@main_bp.route('/decadas')
def decadas():
    # Trae las bandas reales de la BD y las agrupa por decada_principal,
    # para no duplicar esos datos en decadas_data.py.
    todas_las_bandas = Banda.query.order_by(Banda.popularidad.desc()).all()
    bandas_por_decada = {}
    for banda in todas_las_bandas:
        bandas_por_decada.setdefault(banda.decada_principal, []).append(banda)

    return render_template('decadas.html', decadas=DECADAS, bandas_por_decada=bandas_por_decada)


@main_bp.route('/subgeneros')
def subgeneros():
    # Cruza cada subgenero con bandas reales de la BD cuyo campo
    # 'genero' lo mencione (case-insensitive), sin duplicar datos.
    todas_las_bandas = Banda.query.all()
    bandas_por_subgenero = {}
    for sub in SUBGENEROS:
        match = sub['genero_match'].lower()
        coincidencias = [b for b in todas_las_bandas if match in (b.genero or '').lower()]
        bandas_por_subgenero[sub['slug']] = coincidencias

    return render_template('subgeneros.html', subgeneros=SUBGENEROS, bandas_por_subgenero=bandas_por_subgenero)


@main_bp.route('/bandas')
def bandas():
    orden = request.args.get('orden', 'popularidad')
    columnas_validas = {
        'popularidad': Banda.popularidad,
        'grammys': Banda.grammys_totales,
        'ventas': Banda.ventas_estimadas,
        'influencia': Banda.indice_influencia,
    }
    columna = columnas_validas.get(orden, Banda.popularidad)
    lista_bandas = Banda.query.order_by(columna.desc()).all()
    return render_template('bandas.html', bandas=lista_bandas, orden_actual=orden)


@main_bp.route('/artistas')
def artistas():
    lista_artistas = Artista.query.order_by(Artista.anio_nacimiento.asc()).all()
    return render_template('artistas.html', artistas=lista_artistas)


@main_bp.route('/trivia')
def trivia():
    return render_template('trivia.html', preguntas=PREGUNTAS)
