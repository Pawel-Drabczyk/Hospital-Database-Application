import psycopg2
import os


def insertMedicalConditionSQL(medicalConditionDict, user):
    sql = "INSERT INTO hdbapp.medicalCondition(idMedicalCondition, name, isInfectious)" \
          " VALUES(%s, %s, %s);"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
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
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
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
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
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