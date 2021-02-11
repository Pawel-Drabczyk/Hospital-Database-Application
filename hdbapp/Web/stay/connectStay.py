import psycopg2
import os


def insertStaySQL(stayDict, user):
    sql = "INSERT INTO hdbapp.stay(idStay, idPatient, startDate, endDate, idDoctor, idWard)" \
          " VALUES (%s, %s, %s, %s, %s, %s);" \
          "INSERT INTO hdbapp.diseaseStay(idDisease, idStay)" \
          "VALUES (%s, %s);" \


    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (stayDict['idStay'], stayDict['idPatient'], stayDict['startDate'], stayDict['endDate'],
                          stayDict['idDoctor'], stayDict['idWard'], stayDict['idDisease'], stayDict['idStay']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()

def selectStaySQL(stayDict, user):
    sql = "SELECT * FROM hdbapp.optionalSearchStay(%s, %s, %s, %s, %s, %s);"

    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (stayDict['idStay'], stayDict['idPatient'], stayDict['startDate'], stayDict['endDate'],
                          stayDict['idDoctor'], stayDict['idWard']))
        results = cur.fetchall()
        cur.close()
        return results

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def updateStaySQL(stayDict, user):
    sql = "UPDATE hdbapp.stay SET " \
          "(idStay, idPatient, startDate, endDate, idDoctor, idWard) " \
          "= (%s, %s, %s, %s, %s, %s) " \
          "WHERE idStay=%s;" \
          "UPDATE hdbapp.diseaseStay SET" \
          "(idDisease, idStay)" \
          "= (%s, %s)" \
          "where idStay=%s;"

    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (stayDict['idStay'], stayDict['idPatient'], stayDict['startDate'],
                          stayDict['endDate'], stayDict['idDoctor'], stayDict['idWard'],
                          stayDict['idStayOld'], stayDict['idDisease'], stayDict['idStay'], stayDict['idStayOld']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()