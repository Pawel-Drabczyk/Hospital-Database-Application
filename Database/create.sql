DROP SCHEMA IF EXISTS hdbapp CASCADE; -- hospital-database-application
CREATE SCHEMA hdbapp;
SET search_path TO hdbapp;


CREATE TABLE possible_symptoms
    (
    id_possible_symptoms INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    id_medical_condition INT NOT NULL,
    PRIMARY KEY(id_possible_symptoms)
    );

CREATE TABLE medical_condition
    (
    id_medical_condition INT NOT NULL,
    is_infectious BOOLEAN NOT NULL,
    PRIMARY KEY(id_medical_condition)
    );

CREATE TABLE symptoms
    (
    id_symptom INT NOT NULL,
    id_disease INT NOT NULL,
    id_possible_symptoms INT NOT NULL,
    PRIMARY KEY(id_symptom)
    );

CREATE TABLE disease
    (
    id_disease INT NOT NULL,
    id_patient INT NOT NULL,
    start_date DATE,
    end_date DATE,
    additional_symptoms VARCHAR(30),
    id_medical_condition INT NOT NULL,
    id_doctor INT NOT NULL,
    PRIMARY KEY(id_disease)
    );

CREATE TABLE drug
    (
    id_drug INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    dose VARCHAR(30) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    id_disease INT NOT NULL,
    PRIMARY KEY(id_drug)
    );

CREATE TABLE patient
    (
    id_patient INT NOT NULL,
    name VARCHAR(30),
    surname VARCHAR(30),
    gender VARCHAR(2),
    postal_code VARCHAR(30),
    city VARCHAR(30),
    street VARCHAR(30),
    house_number VARCHAR(30),
    apartment_number VARCHAR(30),
    tel VARCHAR(30),
    is_alive BOOLEAN NOT NULL,
    PRIMARY KEY(id_patient)
    );

CREATE TABLE stay
    (
    id_stay INT NOT NULL,
    id_patient INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    id_doctor INT NOT NULL,
    id_ward INT NOT NULL,
    PRIMARY KEY(id_stay)
    );

CREATE TABLE disease_stay
    (
    id_disease_stay INT NOT NULL,
    id_disease INT NOT NULL,
    id_stay INT NOT NULL,
    PRIMARY KEY(id_disease_stay)
    );

CREATE TABLE surgical_operation
    (
    id_surgical_operation VARCHAR(30) NOT NULL,
    name VARCHAR(30),
    description VARCHAR(100),
    id_disease_stay INT NOT NULL,
    PRIMARY KEY(id_surgical_operation)
    );

CREATE TABLE ward
    (
    id_ward INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    capacity INT NOT NULL,
    id_hospital INT NOT NULL,
    PRIMARY KEY(id_ward)
    );

CREATE TABLE doctor
    (
    id_doctor INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    gender VARCHAR(2) NOT NULL,
    tel VARCHAR(30),
    specialisation VARCHAR(30),
    id_ward INT NOT NULL,
    is_hired BOOLEAN NOT NULL,
    PRIMARY KEY(id_doctor)
    );

CREATE TABLE hospital
    (
    id_hospital INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    PRIMARY KEY(id_hospital)
    );

CREATE TABLE administrative_worker
    (
    id_administrative_worker INT NOT NULL,
    id_hospital INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    tel VARCHAR(30) NOT NULL,
    is_main_admin BOOLEAN NOT NULL,
    is_hired BOOLEAN NOT NULL,
    PRIMARY KEY(id_administrative_worker)
    );

ALTER TABLE drug
    ADD FOREIGN KEY (id_disease)
        REFERENCES disease (id_disease);

ALTER TABLE disease
    ADD FOREIGN KEY (id_patient)
        REFERENCES patient (id_patient);

ALTER TABLE disease
    ADD FOREIGN KEY (id_medical_condition)
        REFERENCES medical_condition (id_medical_condition);

ALTER TABLE disease
    ADD FOREIGN KEY (id_doctor)
        REFERENCES doctor (id_doctor);

ALTER TABLE symptoms
    ADD FOREIGN KEY (id_possible_symptoms)
        REFERENCES possible_symptoms (id_possible_symptoms);

ALTER TABLE symptoms
    ADD FOREIGN KEY (id_disease)
        REFERENCES disease (id_disease);

ALTER TABLE possible_symptoms
    ADD FOREIGN KEY (id_medical_condition)
        REFERENCES medical_condition (id_medical_condition);

ALTER TABLE disease_stay
    ADD FOREIGN KEY (id_disease)
        REFERENCES disease (id_disease);

ALTER TABLE disease_stay
    ADD FOREIGN KEY (id_stay)
        REFERENCES stay (id_stay);

ALTER TABLE surgical_operation
    ADD FOREIGN KEY (id_disease_stay)
        REFERENCES disease_stay (id_disease_stay);

ALTER TABLE doctor
    ADD FOREIGN KEY (id_ward)
        REFERENCES ward (id_ward);

ALTER TABLE stay
    ADD FOREIGN KEY (id_patient)
        REFERENCES patient (id_patient);

ALTER TABLE stay
    ADD FOREIGN KEY (id_doctor)
        REFERENCES doctor (id_doctor);

ALTER TABLE stay
    ADD FOREIGN KEY (id_ward)
        REFERENCES ward (id_ward);

ALTER TABLE ward
    ADD FOREIGN KEY (id_hospital)
        REFERENCES hospital (id_hospital);

ALTER TABLE administrative_worker
    ADD FOREIGN KEY (id_hospital)
        REFERENCES hospital (id_hospital);
