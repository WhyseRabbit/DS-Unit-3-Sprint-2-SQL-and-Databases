import sqlite3

df_name = "northwind_small.sqlite3"
conn = sqlite3.connect(df_name)
cursor = conn.cursor()

big_price = cursor.execute(f"""SELECT UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;""")
print(big_price)

average_age = cursor.execute(f"""SELECT
AVG(HireDate - BirthDate) AS YearsOld
FROM Employee""").fetchall()
print(average_age)

conn.commit()
cursor.close()
conn.close()