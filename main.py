from flask import Flask
from step_1.search import search_by_blueprint
from utils import search_actors, search_by

# создаем Фласк приложение
app = Flask(__name__)
# Регистрируем блюпринты
app.register_blueprint(search_by_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=1000)
