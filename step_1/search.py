from flask import Blueprint, jsonify
from utils import get_the_newest_film, get_films_dy_range, get_films_by_rating, search_by_genre

search_by_blueprint = Blueprint('search_by_blueprint', __name__, template_folder="templates")


@search_by_blueprint.route('/movie/<title>')
def search_film(title):
    film = get_the_newest_film(title)
    return jsonify(film)


@search_by_blueprint.route('/movie/<int:first_year>/to/<int:second_year>')
def search_by_range(first_year, second_year):
    films = get_films_dy_range(first_year, second_year)
    return jsonify(films)


@search_by_blueprint.route('/rating/<group>')
def search_by_rating(group):
    films = get_films_by_rating(group)
    return jsonify(films)


@search_by_blueprint.route('/genre/<genre>')
def search_by_genge(genre):
    films = search_by_genre(genre)
    return jsonify(films)
