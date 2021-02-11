import psycopg2
import os


def insertWardSQL(wardDict, user):
    sql = "INSERT INTO hdbapp.ward(idWard, name, capacity, idHospital)" \
          " VALUES(%s, %s, %s, %s);"

    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (wardDict['idWard'], wardDict['name'], wardDict['capacity'], wardDict['idHospital']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()

def selectWardSQL(wardDict, user):
    sql = "select * from hdbapp.optionalSearchWard(%s, %s, %s, %s);"

    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (wardDict['idWard'], wardDict['name'], wardDict['capacity'], wardDict['idHospital']))
        results = cur.fetchall()
        cur.close()
        return results

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def updateWardSQL(wardDict, user):
    sql = "update hdbapp.ward SET " \
          "(idWard, name, capacity, idHospital) " \
          "= (%s, %s, %s, %s) " \
          "WHERE idWard=%s;"

    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (wardDict['idWard'], wardDict['name'], wardDict['capacity'],
                          wardDict['idHospital'], wardDict['idWardOld']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()

