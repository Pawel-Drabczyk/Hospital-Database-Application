import psycopg2
import os

conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()
cur.execute(open("hdbapp/Database/create.sql", "r").read())
conn.commit()
cur.execute(open("hdbapp/Database/functions.sql", "r").read())
conn.commit()
cur.execute(open("hdbapp/Database/views.sql", "r").read())
conn.commit()
cur.execute(open("hdbapp/Database/insert.sql", "r").read())
conn.commit()
cur.close()