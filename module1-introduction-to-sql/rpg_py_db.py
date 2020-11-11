import sqlite3


def db_get(db_name= "rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

def query_exec(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


GET_CHARACTERS = """SELECT
COUNT(DISTINCT character_id)
FROM charactercreator_character;"""

connect = db_get()
cursor = connect.cursor()

character_num = query_exec(cursor, GET_CHARACTERS)
print(f"There are {character_num} characters in this game.")

GET_SUBCLASS = """SELECT
charactercreator_character as char
(SELECT
COUNT(DISTINCT mage.character_ptr_id) as Mages)
FROM
char.character_id
JOIN charactercreator_mage as mage
ON char.character_id = mage.character_ptr_id
GROUP BY Mages;
"""

mage_subclass = query_exec(cursor, GET_SUBCLASS)
print(f"There are {mage_subclass} mages in this data.")

GET_ITEM_NUM = """SELECT
COUNT(DISTINCT item_id)
FROM armory_item;"""

item_num = query_exec(cursor, GET_ITEM_NUM)
print(f"There are {item_num} items in this game.")

GET_WEAPON_NUM = """SELECT
COUNT(weapon.item_ptr_id) as WeaponNum
FROM armory_weapon as weapon
JOIN armory_item as item
ON weapon.item_ptr_id = item.item_id"""

weapon_num = query_exec(cursor, GET_WEAPON_NUM)
print(f"There are {weapon_num} weapons, leaving"\
      f"{item_num} items that aren't weapons.")

