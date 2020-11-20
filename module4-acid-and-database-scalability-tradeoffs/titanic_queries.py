import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OH_NO!")
DB_USER = os.getenv("DB_USER", default="OH_NO!")
DB_PW = os.getenv("DB_PW", default="OH_NO!")
DB_HOST = os.getenv("DB_HOST", default="OH_NO!")

CSV_FILEPATH = "titanic.csv"


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                              password=DB_PW, host=DB_HOST)

cursor = connection.cursor()


def query_execute(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


SURVIVOR_NUM = """
SELECT
COUNT(survived)
FROM titanic_queries
WHERE survived = True;
"""

survivor_count = query_execute(cursor, SURVIVOR_NUM)
print(f"There were {survivor_count} survivors from the Titanic")

PCLASS_NUM = """
SELECT
COUNT(pclass)
FROM titanic_queries
GROUP BY pclass;
"""

pclass_count = query_execute(cursor, PCLASS_NUM)
print("1, 2, 3:", pclass_count)

PCLASS_SORTED_SURVIVORS = """
SELECT
COUNT(pclass),
COUNT(survived)
FROM titanic_queries
WHERE survived = true
GROUP BY pclass;
"""

PCLASS_SORTED_DEATHS = """
SELECT
COUNT(pclass),
COUNT(survived)
FROM titanic_queries
WHERE survived = false
GROUP BY pclass;
"""

sorted_survivors = query_execute(cursor, PCLASS_SORTED_SURVIVORS)
sorted_deaths = query_execute(cursor, PCLASS_SORTED_DEATHS)
print("Survivors/Deaths by Class: 1, 2, 3:", sorted_survivors, sorted_deaths)
