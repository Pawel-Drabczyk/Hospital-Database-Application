CREATE OR REPLACE FUNCTION hdbapp.optionalSearchPatient (idPatientSearched VARCHAR, nameSearched VARCHAR,
                                                        surnameSearched VARCHAR, genderSearched VARCHAR,
                                                        postalCodeSearched VARCHAR, citySearched VARCHAR,
                                                        streetSearched VARCHAR, houseNumberSearched VARCHAR,
                                                        apartmentNumberSearched VARCHAR, telSearched VARCHAR,
                                                        emailSearched VARCHAR, isAliveSearched BOOLEAN)
    RETURNS TABLE (idPatient VARCHAR, name VARCHAR, surname VARCHAR,
                                                        gender VARCHAR, postalCode VARCHAR, city VARCHAR,
                                                        street VARCHAR, houseNumber VARCHAR, apartmentNumber VARCHAR,
                                                        tel VARCHAR, email VARCHAR, additionalDescription VARCHAR,
                                                        isAlive BOOLEAN)
                                                        AS
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