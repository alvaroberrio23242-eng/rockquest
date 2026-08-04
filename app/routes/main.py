from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/historia')
def historia():
    return render_template('historia.html')


@main_bp.route('/linea-del-tiempo')
def linea_del_tiempo():
    return render_template('linea_del_tiempo.html')


@main_bp.route('/decadas')
def decadas():
    return render_template('decadas.html')


@main_bp.route('/subgeneros')
def subgeneros():
    return render_template('subgeneros.html')


@main_bp.route('/bandas')
def bandas():
    return render_template('bandas.html')


@main_bp.route('/artistas')
def artistas():
    return render_template('artistas.html')
