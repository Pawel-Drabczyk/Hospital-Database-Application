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

def insertWardSQL(wardDict, user):
    sql = "INSERT INTO hdbapp.ward(idWard, name, capacity, idHospital)" \
          " VALUES(%s, %s, %s, %s);"

    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
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
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
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
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
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

