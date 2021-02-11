import psycopg2
from configparser import ConfigParser
import os


def config(filename, section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def insertStaySQL(stayDict, user):
    sql = "INSERT INTO hdbapp.stay(idStay, idPatient, startDate, endDate, idDoctor, idWard)" \
          " VALUES (%s, %s, %s, %s, %s, %s);" \
          "INSERT INTO hdbapp.diseaseStay(idDisease, idStay)" \
          "VALUES (%s, %s);" \


    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
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
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
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
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
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