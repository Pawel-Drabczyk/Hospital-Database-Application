import psycopg2

sql = "\i create.sql; \i functions.sql; \i views.sql; \i insert.sql;"

conn = psycopg2.connect(os.getenv(['DATABASE_URL']))
cur = conn.cursor()
cur.execute(sql)
conn.commit()
cur.close()