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


def insertDoctorSQL(doctorDict, user):
    sql = "INSERT INTO hdbapp.doctor(idDoctor, name, surname, gender, " \
          "tel, email, specialisation, idWard)" \
          " VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
    conn = None
    try:
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
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
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
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
        params = config(os.path.join('Users', f'{user}.ini'), 'postgresql')
        conn = psycopg2.connect(**params)
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
