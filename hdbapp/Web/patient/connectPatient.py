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


def insertPatientSQL(patientDict, user):
    sql = "INSERT INTO hdbapp.patient(idPatient, name, surname, gender, " \
          "postalCode, city, street, houseNumber, apartmentNumber, tel, email, additionalDescription, isAlive)" \
          " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (patientDict['idPatient'], patientDict['name'], patientDict['surname'], patientDict['gender'],
                          patientDict['postalCode'], patientDict['city'], patientDict['street'],
                          patientDict['houseNumber'], patientDict['apartmentNumber'], patientDict['tel'],
                          patientDict['email'], patientDict['additionalDescription'], patientDict['isAlive']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()


def selectPatientSQL(patientDict, user):
    sql = "select * from hdbapp.optionalSearchPatient(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (patientDict['idPatient'], patientDict['name'], patientDict['surname'], patientDict['gender'],
                          patientDict['postalCode'], patientDict['city'], patientDict['street'],
                          patientDict['houseNumber'], patientDict['apartmentNumber'], patientDict['tel'],
                          patientDict['email'], patientDict['isAlive']))
        results = cur.fetchall()
        cur.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def updatePatientSQL(patientDict, user):
    sql = "update hdbapp.patient SET " \
          "(idPatient, name, surname, gender, postalCode, city, street, houseNumber," \
          " apartmentNumber, tel, email, additionalDescription, isAlive) " \
          "= (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE idPatient=%s;"
    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (patientDict['idPatient'], patientDict['name'], patientDict['surname'], patientDict['gender'],
                          patientDict['postalCode'], patientDict['city'], patientDict['street'],
                          patientDict['houseNumber'], patientDict['apartmentNumber'], patientDict['tel'],
                          patientDict['email'], patientDict['additionalDescription'], patientDict['isAlive'],
                          patientDict['idPatientOld']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()
