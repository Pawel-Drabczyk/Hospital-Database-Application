CREATE VIEW diseaseSum AS
SELECT hdbapp.medicalCondition.name AS diseaseName,
        Count(*) AS NumberofDiseases ,
        CAST (Count(*) AS FLOAT )/(SELECT COUNT(*) FROM hdbapp.disease) AS PercentofAllDiseases
FROM hdbapp.disease
    JOIN hdbapp.medicalCondition
        USING(idMedicalCondition)
GROUP BY hdbapp.medicalCondition.name;

CREATE VIEW capacityTaken AS
SELECT hdbapp.ward.idWard, hdbapp.ward.name AS WardName, hdbapp.hospital.name AS HospitalName, hdbapp.ward.capacity,
       COUNT(hdbapp.patient.idPatient) AS CapacityTaken,
       CAST (COUNT(hdbapp.patient.idPatient) AS FLOAT)/hdbapp.ward.capacity  AS Ratio
FROM hdbapp.ward
    JOIN hdbapp.hospital USING(idHospital)
    JOIN hdbapp.stay USING (idWard)
    JOIN hdbapp.patient USING (idPatient)
GROUP BY hdbapp.ward.idWard,hdbapp.hospital.name;

CREATE VIEW doctorOccupance AS
SELECT hdbapp.doctor.idDoctor, hdbapp.doctor.name, hdbapp.doctor.surname, hdbapp.doctor.specialisation, COUNT(hdbapp.disease.idPatient) AS Patients
FROM hdbapp.doctor
    JOIN hdbapp.disease USING(idDoctor)
GROUP BY hdbapp.doctor.idDoctor;
