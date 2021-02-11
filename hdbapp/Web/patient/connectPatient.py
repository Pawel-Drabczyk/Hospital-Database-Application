import psycopg2
import os


def insertPatientSQL(patientDict, user):
    sql = "INSERT INTO hdbapp.patient(idPatient, name, surname, gender, " \
          "postalCode, city, street, houseNumber, apartmentNumber, tel, email, additionalDescription, isAlive)" \
          " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
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

        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
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
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
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
