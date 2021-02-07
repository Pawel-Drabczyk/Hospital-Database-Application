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
        params = config(os.path.join('..', 'Users', f'{user}.ini'), 'postgresql')
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

def insertPatient(patientDict, user):
    sql = "INSERT INTO hdbapp.patient(idPatient, name, surname, gender, " \
          "postalCode, city, street, houseNumber, apartmentNumber, tel, email, additionalDescription, isAlive)" \
          " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

    conn = None
    try:
        params = config(os.path.join('..', 'Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (patientDict['idPatient'], patientDict['name'], patientDict['surname'], patientDict['gender'],
                          patientDict['postalCode'], patientDict['city'], patientDict['street'], patientDict['houseNumber'],
                          patientDict['apartmentNumber'], patientDict['email'], patientDict['additionalDescription'],
                          patientDict['tel'], patientDict['isAlive'] ) )
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()


# patient = {
#     'idPatient': '90102399999',
#     'name': None,
#     'surname': None,
#     'gender': None,
#     'postalCode': None,
#     'city': None,
#     'street': None,
#     'houseNumber': None,
#     'apartmentNumber': None,
#     'tel': None,
#     'isAlive': True
# }
