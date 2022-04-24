from flask import Flask
from step_1.search import search_by_name_blueprint, search_by_range_blueprint \
    , search_by_rating_blueprint, search_by_genre_blueprunt
from utils import search_actors,search_by

# создаем Фласк приложение
app = Flask(__name__)
# Регистрируем блюпринты
app.register_blueprint(search_by_name_blueprint)
app.register_blueprint(search_by_range_blueprint)
app.register_blueprint(search_by_rating_blueprint)
app.register_blueprint(search_by_genre_blueprunt)

if __name__ == '__main__':
    app.run(debug=True, port=1000)
