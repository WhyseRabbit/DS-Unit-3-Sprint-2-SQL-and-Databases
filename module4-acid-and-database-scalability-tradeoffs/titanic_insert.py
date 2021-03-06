import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OH_NO!")
DB_USER = os.getenv("DB_USER", default="OH_NO!")
DB_PW = os.getenv("DB_PW", default="OH_NO!")
DB_HOST = os.getenv("DB_HOST", default="OH_NO!")

CSV_FILEPATH = "titanic.csv"


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                              password=DB_PW, host=DB_HOST)

cursor = connection.cursor()


titanic_insert = """
DROP TABLE IF EXISTS titanic_queries;
CREATE TABLE IF NOT EXISTS titanic_queries (
id SERIAL PRIMARY KEY,
survived boolean,
pclass int4,
full_name text,
gender text,
age int4,
sib_spouse_count int4,
parent_child_count int4,
fare float8
);"""


cursor.execute(titanic_insert)


data = pd.read_csv(CSV_FILEPATH)
data["Survived"] = data["Survived"].values.astype(bool)
data = data.astype("object")

tuple_data = list(data.to_records(index=False))

insert_query = """INSERT INTO
titanic_queries (survived, pclass, full_name, gender, age, sib_spouse_count, parent_child_count, fare)
VALUES %s"""

execute_values(cursor, insert_query, tuple_data)

connection.commit()
cursor.close()
connection.close()
