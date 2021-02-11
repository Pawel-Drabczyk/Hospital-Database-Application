import psycopg2
import os

conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()
cur.execute(open("create.sql", "r").read())
conn.commit()
cur.execute(open("functions.sql", "r").read())
conn.commit()
cur.execute(open("views.sql", "r").read())
conn.commit()
cur.execute(open("insert.sql", "r").read())
conn.commit()
cur.close()