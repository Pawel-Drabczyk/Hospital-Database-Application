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

def insertMedicalConditionSQL(medicalConditionDict, user):
    sql = "INSERT INTO hdbapp.medicalCondition(idMedicalCondition, name, isInfectious)" \
          " VALUES(%s, %s, %s);"
    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (medicalConditionDict['idMedicalCondition'], medicalConditionDict['name'],
                          medicalConditionDict['isInfectious']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()

def selectMedicalConditionSQL(medicalConditionDict, user):
    sql = "select * from hdbapp.optionalSearchMedicalCondition(%s, %s, %s);"
    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (medicalConditionDict['idMedicalCondition'], medicalConditionDict['name'],
                          medicalConditionDict['isInfectious']))
        results = cur.fetchall()
        cur.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def updateMedicalConditionSQL(medicalConditionDict, user):
    sql = "update hdbapp.medicalCondition SET " \
          "(idMedicalCondition, name, isInfectious) " \
          "= (%s, %s, %s) " \
          "WHERE idMedicalCondition=%s;"
    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (medicalConditionDict['idMedicalCondition'], medicalConditionDict['name'],
                          medicalConditionDict['isInfectious'], medicalConditionDict['idMedicalConditionOld']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()