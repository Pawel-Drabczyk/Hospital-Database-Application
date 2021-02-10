DROP SCHEMA IF EXISTS hdbapp CASCADE; -- hospital-database-application
CREATE SCHEMA hdbapp;
SET search_path TO hdbapp;


CREATE TABLE possibleSymptoms
    (
    idPossibleSymptoms INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    idMedicalCondition INT NOT NULL,
    PRIMARY KEY(idPossibleSymptoms)
    );

CREATE TABLE medicalCondition
    (
    idMedicalCondition INT NOT NULL,
    isInfectious BOOLEAN NOT NULL,
    PRIMARY KEY(idMedicalCondition)
    );

CREATE TABLE symptoms
    (
    idSymptom INT NOT NULL,
    idDisease INT NOT NULL,
    idPossibleSymptoms INT NOT NULL,
    PRIMARY KEY(idSymptom)
    );

CREATE TABLE disease
    (
    idDisease INT NOT NULL,
    idPatient VARCHAR(30) NOT NULL,
    startDate DATE,
    endDate DATE,
    additionalSymptoms VARCHAR(30),
    idMedicalCondition INT NOT NULL,
    idDoctor VARCHAR NOT NULL,
    PRIMARY KEY(idDisease)
    );

CREATE TABLE drug
    (
    idDrug INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    dose VARCHAR(30) NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    idDisease INT NOT NULL,
    PRIMARY KEY(idDrug)
    );

CREATE TABLE patient
    (
    idPatient VARCHAR(30) NOT NULL,
    name VARCHAR(30),
    surname VARCHAR(30),
    gender VARCHAR(2),
    postalCode VARCHAR(30),
    city VARCHAR(30),
    street VARCHAR(30),
    houseNumber VARCHAR(30),
    apartmentNumber VARCHAR(30),
    tel VARCHAR(30),
    email VARCHAR(30),
    additionalDescription VARCHAR(30),
    isAlive BOOLEAN NOT NULL,
    PRIMARY KEY(idPatient)
    );

CREATE TABLE stay
    (
    idStay INT NOT NULL,
    idPatient VARCHAR(30) NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE,
    idDoctor VARCHAR NOT NULL,
    idWard INT NOT NULL,
    PRIMARY KEY(idStay)
    );

CREATE TABLE diseaseStay
    (
    idDiseaseStay INT NOT NULL,
    idDisease INT NOT NULL,
    idStay INT NOT NULL,
    PRIMARY KEY(idDiseaseStay)
    );

CREATE TABLE surgicalOperation
    (
    idSurgicalOperation VARCHAR(30) NOT NULL,
    name VARCHAR(30),
    description VARCHAR(100),
    idDiseaseStay INT NOT NULL,
    PRIMARY KEY(idSurgicalOperation)
    );

CREATE TABLE ward
    (
    idWard INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    capacity INT NOT NULL,
    idHospital INT NOT NULL,
    PRIMARY KEY(idWard)
    );

CREATE TABLE doctor
    (
    idDoctor VARCHAR NOT NULL,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    gender VARCHAR(2) NOT NULL,
    tel VARCHAR(30),
    email VARCHAR(30),
    specialisation VARCHAR(30),
    idWard INT NOT NULL,
    PRIMARY KEY(idDoctor)
    );

CREATE TABLE hospital
    (
    idHospital INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    PRIMARY KEY(idHospital)
    );

CREATE TABLE administrativeWorker
    (
    idAdministrativeWorker INT NOT NULL,
    idHospital INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    tel VARCHAR(30) NOT NULL,
    isMainAdmin BOOLEAN NOT NULL,
    isHired BOOLEAN NOT NULL,
    PRIMARY KEY(idAdministrativeWorker)
    );

ALTER TABLE drug
    ADD FOREIGN KEY (idDisease)
        REFERENCES disease (idDisease);

ALTER TABLE disease
    ADD FOREIGN KEY (idPatient)
        REFERENCES patient (idPatient);

ALTER TABLE disease
    ADD FOREIGN KEY (idMedicalCondition)
        REFERENCES medicalCondition (idMedicalCondition);

ALTER TABLE disease
    ADD FOREIGN KEY (idDoctor)
        REFERENCES doctor (idDoctor);

ALTER TABLE symptoms
    ADD FOREIGN KEY (idPossibleSymptoms)
        REFERENCES possibleSymptoms (idPossibleSymptoms);

ALTER TABLE symptoms
    ADD FOREIGN KEY (idDisease)
        REFERENCES disease (idDisease);

ALTER TABLE possibleSymptoms
    ADD FOREIGN KEY (idMedicalCondition)
        REFERENCES medicalCondition (idMedicalCondition);

ALTER TABLE diseaseStay
    ADD FOREIGN KEY (idDisease)
        REFERENCES disease (idDisease);

ALTER TABLE diseaseStay
    ADD FOREIGN KEY (idStay)
        REFERENCES stay (idStay);

ALTER TABLE surgicalOperation
    ADD FOREIGN KEY (idDiseaseStay)
        REFERENCES diseaseStay (idDiseaseStay);

ALTER TABLE doctor
    ADD FOREIGN KEY (idWard)
        REFERENCES ward (idWard);

ALTER TABLE stay
    ADD FOREIGN KEY (idPatient)
        REFERENCES patient (idPatient);

ALTER TABLE stay
    ADD FOREIGN KEY (idDoctor)
        REFERENCES doctor (idDoctor);

ALTER TABLE stay
    ADD FOREIGN KEY (idWard)
        REFERENCES ward (idWard);

ALTER TABLE ward
    ADD FOREIGN KEY (idHospital)
        REFERENCES hospital (idHospital);

ALTER TABLE administrativeWorker
    ADD FOREIGN KEY (idHospital)
        REFERENCES hospital (idHospital);
