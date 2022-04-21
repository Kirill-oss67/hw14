from flask import Flask
from step_1.search import search_blueprint

# создаем Фласк приложение
app = Flask(__name__)
# Регистрируем блюпринты
app.register_blueprint(search_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=1000)

# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
