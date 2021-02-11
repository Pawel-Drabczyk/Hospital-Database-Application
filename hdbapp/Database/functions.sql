CREATE OR REPLACE FUNCTION hdbapp.optionalSearchPatient (idPatientSearched VARCHAR, nameSearched VARCHAR,
                                                        surnameSearched VARCHAR, genderSearched VARCHAR,
                                                        postalCodeSearched VARCHAR, citySearched VARCHAR,
                                                        streetSearched VARCHAR, houseNumberSearched VARCHAR,
                                                        apartmentNumberSearched VARCHAR, telSearched VARCHAR,
                                                        emailSearched VARCHAR, isAliveSearched BOOLEAN)
    RETURNS TABLE (idPatient VARCHAR, name VARCHAR, surname VARCHAR, gender VARCHAR, postalCode VARCHAR, city VARCHAR,
                   street VARCHAR, houseNumber VARCHAR, apartmentNumber VARCHAR, tel VARCHAR, email VARCHAR,
                   additionalDescription VARCHAR, isAlive BOOLEAN) AS
$$
BEGIN
    RETURN QUERY
        SELECT * FROM hdbapp.patient
               WHERE
                   (hdbapp.patient.idPatient=idPatientSearched OR idPatientSearched IS NULL)
                   AND (hdbapp.patient.name=nameSearched OR nameSearched IS NULL)
                   AND (hdbapp.patient.surname=surnameSearched OR surnameSearched IS NULL)
                   AND (hdbapp.patient.gender=genderSearched OR genderSearched IS NULL OR genderSearched='B')
                   AND (hdbapp.patient.postalCode=postalCodeSearched OR postalCodeSearched IS NULL)
                   AND (hdbapp.patient.city=citySearched OR citySearched IS NULL)
                   AND (hdbapp.patient.street=streetSearched OR streetSearched IS NULL)
                   AND (hdbapp.patient.houseNumber=houseNumberSearched OR houseNumberSearched IS NULL)
                   AND (hdbapp.patient.apartmentNumber=apartmentNumberSearched OR apartmentNumberSearched IS NULL)
                   AND (hdbapp.patient.tel=telSearched OR telSearched IS NULL)
                   AND (hdbapp.patient.email=emailSearched OR emailSearched IS NULL)
                   AND (hdbapp.patient.isAlive=isAliveSearched OR isAliveSearched IS NULL);
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION hdbapp.optionalSearchDoctor (idDoctorSearched VARCHAR, nameSearched VARCHAR,
                                                        surnameSearched VARCHAR, genderSearched VARCHAR,
                                                        telSearched VARCHAR, emailSearched VARCHAR, specialisationSearched VARCHAR, idWardSearched VARCHAR)

    RETURNS TABLE (idDoctor VARCHAR, name VARCHAR, surname VARCHAR, gender VARCHAR, tel VARCHAR, email VARCHAR,
                    specialisation VARCHAR, idWard INTEGER) AS
$$
BEGIN
    RETURN QUERY
        SELECT * FROM hdbapp.doctor
               WHERE
                   (hdbapp.doctor.idDoctor=idDoctorSearched OR idDoctorSearched IS NULL)
                   AND (hdbapp.doctor.name=nameSearched OR nameSearched IS NULL)
                   AND (hdbapp.doctor.surname=surnameSearched OR surnameSearched IS NULL)
                   AND (hdbapp.doctor.gender=genderSearched OR genderSearched IS NULL OR genderSearched='B')
                   AND (hdbapp.doctor.tel=telSearched OR telSearched IS NULL)
                   AND (hdbapp.doctor.email=emailSearched OR emailSearched IS NULL)
                   AND (hdbapp.doctor.idWard=CAST(idWardSearched AS INTEGER) OR idWardSearched IS NULL);
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION hdbapp.optionalSearchHospital (idHospitalSearched VARCHAR, nameSearched VARCHAR)
    RETURNS TABLE (idHospital INTEGER, name VARCHAR) AS
$$
BEGIN
    RETURN QUERY
        SELECT * FROM hdbapp.hospital
               WHERE
                   (hdbapp.hospital.idHospital=CAST(idHospitalSearched AS INTEGER) OR idHospitalSearched IS NULL)
                   AND (hdbapp.hospital.name=nameSearched OR nameSearched IS NULL);
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION hdbapp.optionalSearchWard (idWardSearched VARCHAR, nameSearched VARCHAR,
                                                     capacitySearched VARCHAR, idHospitalSearched VARCHAR)
    RETURNS TABLE (idWard INTEGER, name VARCHAR, capacity INTEGER, idHospital INTEGER) AS
$$
BEGIN
    RETURN QUERY
        SELECT * FROM hdbapp.ward
               WHERE
                   (hdbapp.ward.idWard=CAST(idWardSearched AS INTEGER) OR idWardSearched IS NULL)
                   AND (hdbapp.ward.name=nameSearched OR nameSearched IS NULL)
                   AND (hdbapp.ward.capacity=CAST(capacitySearched AS INTEGER) OR capacitySearched IS NULL)
                   AND (hdbapp.ward.idHospital=CAST(idHospitalSearched AS INTEGER) OR idHospitalSearched IS NULL);
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION hdbapp.optionalSearchMedicalCondition (idMedicalConditionSearched VARCHAR,
                                                                 nameSearched VARCHAR, isInfectiousSearched VARCHAR)
    RETURNS TABLE (idMedicalCondition INTEGER, name VARCHAR, isInfectious BOOLEAN) AS
$$
BEGIN
    RETURN QUERY
        SELECT * FROM hdbapp.medicalCondition
               WHERE
                   (hdbapp.medicalCondition.idMedicalCondition=CAST(idMedicalConditionSearched AS INTEGER) OR idMedicalConditionSearched IS NULL)
                   AND (hdbapp.medicalCondition.name=nameSearched OR nameSearched IS NULL)
                   AND (hdbapp.medicalCondition.isInfectious=CAST(isInfectiousSearched AS BOOLEAN) OR isInfectiousSearched IS NULL);
END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION hdbapp.optionalSearchDisease (idDiseaseSearched VARCHAR, idPatientSearched VARCHAR,
                                                        startDateSearched VARCHAR, endDateSearched VARCHAR,
                                                        idMedicalConditionSearched VARCHAR, idDoctorSearched VARCHAR)
    RETURNS TABLE (idDisease INTEGER, idPatient VARCHAR, startDate DATE, endDate DATE, idMedicalCondition INTEGER,
                  idDoctor VARCHAR) AS
$$
BEGIN
    RETURN QUERY
        SELECT * FROM hdbapp.disease
               WHERE
                   (hdbapp.disease.idDisease=CAST(idDiseaseSearched AS INTEGER) OR idDiseaseSearched IS NULL)
                   AND (hdbapp.disease.idPatient=idPatientSearched OR idPatientSearched IS NULL)
                   AND (hdbapp.disease.startDate=CAST(startDateSearched AS DATE) OR startDateSearched IS NULL)
                   AND (hdbapp.disease.endDate=CAST(endDateSearched AS DATE) OR endDateSearched IS NULL)
                   AND (hdbapp.disease.idMedicalCondition=CAST(idMedicalConditionSearched AS INTEGER) OR idMedicalConditionSearched IS NULL)
                   AND (hdbapp.disease.idDoctor=idDoctorSearched OR idDoctorSearched IS NULL);
END;
$$ LANGUAGE 'plpgsql';