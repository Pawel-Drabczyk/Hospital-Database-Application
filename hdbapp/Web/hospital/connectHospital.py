import psycopg2
import os


def insertHospitalSQL(hospitalDict, user):
    sql = "INSERT INTO hdbapp.hospital(idHospital, name)" \
          " VALUES(%s, %s);"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (hospitalDict['idHospital'], hospitalDict['name']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()

def selectHospitalSQL(hospitalDict, user):
    sql = "select * from hdbapp.optionalSearchHospital(%s, %s);"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, ( hospitalDict['idHospital'], hospitalDict['name']))
        results = cur.fetchall()
        cur.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def updateHospitalSQL(hospitalDict, user):
    sql = "update hdbapp.hospital SET " \
          "(idHospital, name) " \
          "= (%s, %s) " \
          "WHERE idHospital=%s;"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (hospitalDict['idHospital'], hospitalDict['name'], hospitalDict['idHospitalOld']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()