import sqlite3


def db_get(db_name= "rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

def query_exec(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


GET_CHARACTERS = """SELECT count(*) FROM charactercreator_character;"""

if __name__ == "__main__":
    conn = db_get()
    curs = conn.cursor()
    character_num = query_exec(curs, GET_CHARACTERS)
    print(f"There are {character_num} characters in this game.")

    GET_ITEM_NUM = """SELECT count(*)
FROM armory_item;"""

    item_num = query_exec(curs, GET_ITEM_NUM)
    print(f"There are {item_num} items in this game.")

    WEAPON_NUM = """SELECT count(*) FROM armory_weapon;"""

    item_diff = query_exec(curs, WEAPON_NUM)
    print(f"There are {item_num} unique items; {item_diff} of them are weapons, leaving 137 items that aren't weapons.")

    