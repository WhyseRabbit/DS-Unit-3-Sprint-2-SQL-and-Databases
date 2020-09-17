import sqlite3
import psycopg2

def db_get(db_name= "rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

def query_exec(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

get_toons = """SELECT *
FROM charactercreator_character;"""

if __name__ == "__main__":
    conn = db_get()
    curs = conn.cursor()
    characters = query_exec(curs, get_toons)

print(len(characters))