from flask import render_template, url_for, flash, redirect, session
from hdbapp.Web.statistics.connectStatistics import capacitySQL, diseaseSumSQL, doctorOccupanceSQL


def statistics():
    return render_template('statistics/statistics.html', title='Statistics')

def capacity():
    capacityTupleList = capacitySQL('postgres')
    capacityDictList = []
    i = 1
    for t in capacityTupleList:
        temp = {
            'listNumber': i,
            'idWard': t[0],
            'wardName': t[1],
            'hospitalName': t[2],
            'capacity': t[3],
            'capacityTaken': t[4],
            'ratio': t[5],
        }
        i = i+1
        capacityDictList.append(temp)
    return render_template('statistics/capacity.html', title='Capacity of the wards', capacityDictList=capacityDictList)


def diseaseSum():
    diseaseSumTupleList = diseaseSumSQL('postgres')
    diseaseSumDictList = []
    i = 1
    for t in diseaseSumTupleList:
        temp = {
            'listNumber': i,
            'diseaseName': t[0],
            'numberOfAllDiseases': t[1],
            'percentOfAllDiseases': t[2]
        }
        i = i+1
        diseaseSumDictList.append(temp)
    return render_template('statistics/diseaseSum.html', title='Capacity of the wards', diseaseSumDictList=diseaseSumDictList)


def doctorOccupance():
    doctorOccupanceTupleList = doctorOccupanceSQL('postgres')
    doctorOccupanceDictList = []
    i = 1
    for t in doctorOccupanceTupleList:
        temp = {
            'listNumber': i,
            'idDoctor': t[0],
            'name': t[1],
            'surname': t[2],
            'specialisation': t[3],
            'numberOfPatients': t[4]
        }
        i = i+1
        doctorOccupanceDictList.append(temp)
    return render_template('statistics/doctorOccupance.html', title='Doctor occupance', doctorOccupanceDictList=doctorOccupanceDictList)