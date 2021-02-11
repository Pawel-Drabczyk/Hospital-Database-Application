import psycopg2
import os


def insertDiseaseSQL(diseaseDict, user):
    sql = "INSERT INTO hdbapp.disease(idDisease, idPatient, startDate, endDate, idMedicalCondition, idDoctor)" \
          " VALUES (%s, %s, %s, %s, %s, %s);"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
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
    sql = "select * from hdbapp.optionalSearchDisease(%s, %s, %s, %s, %s, %s);"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
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
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
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

