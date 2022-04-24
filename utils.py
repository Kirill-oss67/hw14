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


def get_films_dy_range(first_year, second_year):
    """Получаем 2 аргумента как года , в диапазоне, которых формируем запрос.
    Получаем и сохраняем данные о фильмах в списке словарей"""
    sqlite_query = f"""SELECT title,release_year
                            FROM netflix 
                            WHERE release_year BETWEEN '{first_year}' AND '{second_year}' 
                            AND `type`='Movie'
                            LIMIT 100 """
    gotten_data = sqlite3_start_connection(sqlite_query)
    lict_films = []
    dict_film = {}
    for i in gotten_data:
        dict_film['title'] = i[0]
        dict_film['release_year'] = i[1]
        lict_films.append(dict_film)
    return lict_films


def get_films_by_rating(group):
    """Получаем группу рейтинга по аргументу функции , формируем запрос.
    Получаем и сохраняем данные о фильмах в списке словарей """
    dict_group = {'children': '"G"',
                  'family': '"G", "PG", "PG-13"',
                  'adult': '"R", "NC-17"'}
    group_rating = dict_group[group]
    sqlite_query = f"""SELECT title,rating, description
                                FROM netflix
                                WHERE rating IN ({group_rating})
                                AND `type`='Movie'
                                LIMIT 100 """
    gotten_data = sqlite3_start_connection(sqlite_query)
    lict_films = []
    dict_film = {}
    for i in gotten_data:
        dict_film['title'] = i[0]
        dict_film['rating'] = i[1]
        dict_film['description'] = i[2]
        lict_films.append(dict_film)
    return lict_films


def search_by_genre(genre):
    """получаем название жанра и формируем запрос. Получаем и сохраняем данные о фильмах в списке словарей"""
    sqlite_query = f"""SELECT title, description, release_year, listed_in
                                    FROM netflix
                                    WHERE listed_in LIKE "%{genre}%"
                                    AND `type`='Movie' 
                                    ORDER BY release_year DESC
                                    LIMIT 10 """
    gotten_data = sqlite3_start_connection(sqlite_query)
    lict_films = []
    dict_film = {}
    for i in gotten_data:
        dict_film['title'] = i[0]
        dict_film['description'] = i[1]
        lict_films.append(dict_film)
    return lict_films

def search_actors(first_actor, second_actor):
    sqlite_query = f"""SELECT `cast`
                       FROM netflix
                       WHERE `cast` LIKE '%{first_actor}%'
                       AND `cast` LIKE '%{second_actor}%'
                                        """
    gotten_data = sqlite3_start_connection(sqlite_query)
    lict_actors = []
    for cast in gotten_data:
        lict_actors.extend(cast[0].split(', '))
    result = []
    for actor in lict_actors:
        if actor not in [first_actor,second_actor]:
            if lict_actors.count(actor) > 2:
                result.append(actor)
    result = set(result)
    return result

def search_by(type,release_year, genre):
    """Поиск по типу , года выпуска, и жанру"""
    sqlite_query = f"""SELECT title, description, release_year, listed_in
                                        FROM netflix
                                        WHERE listed_in LIKE "%{genre}%"
                                        AND `type` LIKE "%{type}%"
                                        AND release_year LIKE "%{release_year}%"
                                """
    gotten_data = sqlite3_start_connection(sqlite_query)
    lict_films = []
    dict_film = {}
    for i in gotten_data:
        dict_film['title'] = i[0]
        dict_film['description'] = i[1]
        lict_films.append(dict_film)
    return lict_films





