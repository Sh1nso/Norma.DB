import sqlite3

titles_list = [
    "идентификатор животного",
    "возраст животного на момент прибытия в приют",
    "кличка",
    "дата рождения",
    "месяц прибытия",
    "год прибытия",
    "тип животного",
    "порода",
    "цвет 1",
    "цвет 2",
    "программа, в которой участвует животное",
    "что сейчас с животным"
]


def find_by_id(id) -> dict:
    """Данная функция возвращает всю информацию по
    животному с переданным id"""
    with sqlite3.connect("data/animals.db") as con:
        cur = con.cursor()
        sqlite_query = """
                        SELECT 
                       animals_final.animal_id,
                       animals_final.age_upon_outcome, animals_final.name,
                       animals_final.date_of_birth, animals_final.outcome_month,
                       animals_final.outcome_year,
                       animal_type.name, animal_breed.name,
                       ac1.name as color_name,
                       outcome_subtype.name,
                       outcome_type.name
                       FROM animals_final
                       LEFT JOIN animal_breed ON animals_final.breed_id = animal_breed.id
                       LEFT JOIN animal_type ON animals_final.type_id = animal_type.id
                       LEFT JOIN animal_color as ac1 ON animals_final.color1_id = ac1.id
                       LEFT JOIN animal_color as ac2 ON animals_final.color2_id = ac2.id
                       LEFT JOIN outcome_subtype ON animals_final.outcome_subtype_id = outcome_subtype.id
                       LEFT JOIN outcome_type ON animals_final.outcome_type_id = outcome_type.id
                       WHERE animals_final.id = ?
                        """
        cur.execute(sqlite_query, (id,))
        data = cur.fetchall()
        s = dict(zip(titles_list, data[0]))
    return s


print(find_by_id(1))
