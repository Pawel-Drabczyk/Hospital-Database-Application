import psycopg2
import os


def insertDoctorSQL(doctorDict, user):
    sql = "INSERT INTO hdbapp.doctor(idDoctor, name, surname, gender, " \
          "tel, email, specialisation, idWard)" \
          " VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (doctorDict['idDoctor'], doctorDict['name'], doctorDict['surname'], doctorDict['gender'],
                          doctorDict['tel'], doctorDict['email'], doctorDict['specialisation'], doctorDict['idWard']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()

def selectDoctorSQL(doctorDict, user):
    sql = "select * from hdbapp.optionalSearchDoctor(%s, %s, %s, %s, %s, %s, %s, %s);"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (doctorDict['idDoctor'], doctorDict['name'], doctorDict['surname'], doctorDict['gender'],
                          doctorDict['tel'], doctorDict['email'], doctorDict['specialisation'], doctorDict['idWard']))
        results = cur.fetchall()
        cur.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def updateDoctorSQL(doctorDict, user):
    sql = "update hdbapp.doctor SET " \
          "(idDoctor, name, surname, gender, tel, email, specialisation, idWard) " \
          "= (%s, %s, %s, %s, %s, %s, %s, %s) WHERE idDoctor=%s;"
    conn = None
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        cur = conn.cursor()
        cur.execute(sql, (doctorDict['idDoctor'], doctorDict['name'], doctorDict['surname'], doctorDict['gender'],
                          doctorDict['tel'], doctorDict['email'], doctorDict['specialisation'], doctorDict['idWard'],
                          doctorDict['idDoctorOld']))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return psycopg2.errors.IntegrityError
    finally:
        if conn is not None:
            conn.close()
