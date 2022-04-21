import sqlite3


def sqlite3_start_connection(sqlite_query):
    """устанавливаем соединение и делаем запрос с параметром аргумента функции"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        sqlite_query = sqlite_query  # используем наш запрос
        cursor.execute(sqlite_query)
        result = cursor.fetchall()
        return result


def get_the_newest_film(title):
    """получаем название фильма и формируем запрос. Получаем и сохраняем данные о фильме в словаре"""
    sqlite_query = f"""SELECT title, country, MAX(release_year), listed_in, description
                        FROM netflix 
                        WHERE title LIKE '%{title}%'
                        AND `type`='Movie'
                        LIMIT 1 """
    gotten_data = sqlite3_start_connection(sqlite_query)
    dict_film = {}
    for i in gotten_data:
        dict_film["title"] = i[0]
        dict_film["country"] = i[1]
        dict_film["release_year"] = i[2]
        dict_film["genre"] = i[3]
        dict_film["description"] = i[4]
    return dict_film
