from flask import Blueprint, jsonify
from utils import get_the_newest_film

search_blueprint = Blueprint('search_blueprint', __name__, template_folder="templates")


@search_blueprint.route('/movie/<title>')
def search_film(title):
    film = get_the_newest_film(title)
    return jsonify(film)