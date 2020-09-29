import sqlite3

db_name = "whyse_demo_data.sqlite3"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

DROP = f"""DROP TABLE IF EXISTS whyse_demo_data.sqlite3;"""

cursor.execute(DROP).fetchall()

CREATE = f"""
CREATE TABLE IF NOT EXISTS "whyse_demo_data.sqlite3" (
"s"	TEXT,
"x"	INTEGER NOT NULL,
"y"	INTEGER NOT NULL,
PRIMARY KEY("s")
);
"""

cursor.execute(CREATE).fetchall()

INSERT1 = f"""
INSERT INTO
"whyse_demo_data.sqlite3" (s, x, y)
VALUES ('g', 3, 9);"""

cursor.execute(INSERT1)

INSERT2 = f"""
INSERT INTO
"whyse_demo_data.sqlite" (s, x, y)
VALUES ('v', 5, 7);"""

cursor.execute(INSERT2)

INSERT3 = f"""
INSERT INTO
"whyse_demo_data.sqlite" (s, x, y)
VALUES ('f', 8, 7);"""

cursor.execute(INSERT3)

conn.commit()

# ROW_COUNT = f"""SELECT
# COUNT(s)
# FROM whyse_demo_data.sqlite3;"""
# total_rows = cursor.execute(ROW_COUNT)
#
# print(f"There are {total_rows} in the dataframe.")

cursor.close()
conn.close()
