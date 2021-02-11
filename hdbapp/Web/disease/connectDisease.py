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

def insertDiseaseSQL(diseaseDict, user):
    sql = "INSERT INTO hdbapp.disease(idDisease, idPatient, startDate, endDate, idMedicalCondition, idDoctor)" \
          " VALUES (%s, %s, %s, %s, %s, %s);"

    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (diseaseDict['idDisease'], diseaseDict['idPatient'], diseaseDict['startDate'],
                          diseaseDict['endDate'], diseaseDict['idMedicalCondition'], diseaseDict['idDoctor']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()

def selectDiseaseSQL(diseaseDict, user):
    sql = "select * from hdbapp.optionalSearchDisease(%s, %s, %s, %s, %s, %s);" \

    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (diseaseDict['idDisease'], diseaseDict['idPatient'], diseaseDict['startDate'],
                          diseaseDict['endDate'], diseaseDict['idMedicalCondition'], diseaseDict['idDoctor']))
        results = cur.fetchall()
        cur.close()
        return results

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def updateDiseaseSQL(diseaseDict, user):
    sql = "update hdbapp.disease SET " \
          "(idDisease, idPatient, startDate, endDate, idMedicalCondition, idDoctor) " \
          "= (%s, %s, %s, %s, %s, %s) " \
          "WHERE idDisease=%s;"

    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (diseaseDict['idDisease'], diseaseDict['idPatient'], diseaseDict['startDate'],
                          diseaseDict['endDate'], diseaseDict['idMedicalCondition'], diseaseDict['idDoctor'],
                          diseaseDict['idDiseaseOld']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()

