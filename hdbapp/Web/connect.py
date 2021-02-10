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


def getDB(user):
    conn = None
    try:
        params = config(os.path.join('../..', 'Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

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
                          patientDict['postalCode'], patientDict['city'], patientDict['street'], patientDict['houseNumber'],
                          patientDict['apartmentNumber'], patientDict['tel'], patientDict['email'],
                          patientDict['additionalDescription'], patientDict['isAlive'] ) )
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()

def selectPatientSQL(patientDict, user):
    sql = "SELECT * FROM hdbapp.patient " \
          "     WHERE " \
          "         (idPatient=%s OR %s IS NULL) " \
          "         AND (name=%s OR %s IS NULL) " \
          "         AND (surname=%s OR %s IS NULL) " \
          "         AND (gender=%s OR %s IS NULL OR %s='B') " \
          "         AND (postalCode=%s OR %s IS NULL) " \
          "         AND (city=%s OR %s IS NULL) " \
          "         AND (street=%s OR %s IS NULL) " \
          "         AND (houseNumber=%s OR %s IS NULL) " \
          "         AND (apartmentNumber=%s OR %s IS NULL) " \
          "         AND (tel=%s OR %s IS NULL) " \
          "         AND (email=%s OR %s IS NULL) " \
          "         AND (isAlive=%s OR %s IS NULL);"

    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (patientDict['idPatient'], patientDict['idPatient'], patientDict['name'], patientDict['name'],
                          patientDict['surname'], patientDict['surname'], patientDict['gender'], patientDict['gender'],
                          patientDict['gender'], patientDict['postalCode'], patientDict['postalCode'], patientDict['city'],
                          patientDict['city'], patientDict['street'], patientDict['street'], patientDict['houseNumber'],
                          patientDict['houseNumber'], patientDict['apartmentNumber'], patientDict['apartmentNumber'],
                          patientDict['tel'], patientDict['tel'], patientDict['email'], patientDict['email'],
                          patientDict['isAlive'], patientDict['isAlive']))
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
#
# patient = {
#     'idPatient': 12345678912,
#     'name': None,
#     'surname': None,
#     'gender': 'B',
#     'postalCode': None,
#     'city': None,
#     'street': None,
#     'houseNumber': None,
#     'apartmentNumber': None,
#     'tel': None,
#     'email': None,
#     'additionalDescription': 'updated from updatePatient()',
#     'isAlive': True,
#     'idPatientOld': '33333333333'
# }
#updatePatient(patient, 'postgres')
#
# patientResultList = selectPatient(patient, 'postgres')
# print(patientResultList)
# for patientTuple in patientResultList:
#     for i in patientTuple:
#         print(i)
