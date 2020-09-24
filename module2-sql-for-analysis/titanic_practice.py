import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OH_NO!")
DB_USER = os.getenv("DB_USER", default="OH_NO!")
DB_PW = os.getenv("DB_PW", default="OH_NO!")
DB_HOST = os.getenv("DB_HOST", default="OH_NO!")

CSV_FILEPATH = "titanic.csv"


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)
print(type(connection))

cursor = connection.cursor()
print(type(cursor))


titan_sql = """
DROP TABLE IF EXISTS titanic_practice;
CREATE TABLE IF NOT EXISTS titanic_practice (
    id SERIAL PRIMARY KEY,
    survived boolean,
    pclass int4,
    full_name text,
    gender text,
    age int4,
    sib_spouse_count int4,
    parent_child_count int4,
    fare float8
);
"""


cursor.execute(titan_sql)


data = pandas.read_csv(CSV_FILEPATH)
data["Survived"] = data["Survived"].values.astype(bool)
data = data.astype("object")
print(data.columns.tolist())

tuple_data = list(data.to_records(index=False))

insert_query = f"""INSERT INTO
titanic_practice (survived, pclass, full_name, gender, age, sib_spouse_count, parent_child_count, fare)
VALUES %s"""

execute_values(cursor, insert_query, tuple_data)

connection.commit()
cursor.close()
connection.close()


######################################DO NOT DO THIS!!!!!#######################################################


# import psycopg2
#
# DB_NAME = "nxbwnxng"
# DB_USER = "nxbwnxng"
# DB_PASS = "33E4H6D_wF7NYnSjhknkOunR4FK7dCLi"
# DB_HOST = "rogue.db.elephantsql.com"
#
# conn = psycopg2.connect(dbname=DB_NAME,
#                         user=DB_NAME,
#                         password=DB_PASS,
#                         host=DB_HOST)
#
# cur = conn.cursor()
#
# cur.execute("SELECT * FROM test_table;")
#
# cur.fetchone()
