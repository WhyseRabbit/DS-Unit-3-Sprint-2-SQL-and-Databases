import psycopg2

conn = psycopg2.connect(dbname="nxbwnxng",
                        user="nxbwnxng",
                        password="33E4H6D_wF7NYnSjhknkOunR4FK7dCLi",
                        host="rogue.db.elephantsql.com")

cur = conn.cursor()

cur.execute("SELECT * FROM test_table;")

cur.fetchone()
