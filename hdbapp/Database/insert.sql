INSERT INTO hdbapp.patient(idPatient, name, surname, gender, postalCode, city, street, houseNumber, apartmentNumber,
            tel, email, additionalDescription, isAlive)
VALUES
('71083086034', 'Evan', 'Black', 'M', 'TA3 9JP', 'NORTH CURRY', 'Cambridge Road', '55','1','736999504','evan.black@gmail.com', 'Football player',TRUE),
('94040472952', 'Libby', 'Cole', 'F', 'YO7 8YR' , 'Dalton', 'West Lane', '59', '54', '784659793', 'libby.cole@gmail.com',NULL, TRUE),
('81141105691', 'Niamh', 'Craig', 'M', 'SA48 5FN', 'Silian', 'Stroude Road', '61', '23', '769405634', 'niamh.craig@gmail.com', NULL, TRUE),
('93210524563', 'Callum', 'Martin' ,'M', 'IP18 8BE', 'Mount Pleasant', 'Hendford Hill', '31', '8', '782625924', 'callum.martin@gmail.com',NULL, TRUE),
('86111174034', 'Sam', 'Warren', 'M', 'CA4 9QF', 'LOW HESKET', 'Souterhead Road', '128', '15', '719130686', 'sam.warren@gmail.com', NULL, TRUE),
('87102589205', 'Ellie', 'Perry', 'F', 'PE19 1TU', 'Little Barford', 'Victoria Road', '37', '7', '726986902', 'ellie.perry@gmail.com', NULL, TRUE),
('93080583665', 'Molly', 'Lamb', 'F', 'NR29 8PP', 'THRIGBY', 'High St', '54', '9', '785598309', 'mollie.lamb@gmail.com', NULL, TRUE),
('61072586373', 'Adam', 'Watkins', 'M', 'E6 7QY', 'London', 'Guild Street', '29', '24', '786275891',NULL,  NULL, FALSE),
('51102609256', 'Alice', 'Lawson', 'F', 'G1 2EG', 'Glasgow', 'Nith Street', '24', '3', '772188110',NULL, NULL, TRUE),
('65122058204', 'Melissa', 'Dale', 'F', 'EH1 5PP', 'EDINBURGH', 'Park Row', '69', '52', '794196183', 'melissa.dale@gmail.com', NULL, TRUE),
('87022148571', 'Leo', 'Hodgson', 'M', 'L3 8QP', 'Liverpool', 'Overton Circle', '25', '8', '776395365', 'leo.hodgson@gmail.com', 'Likes whiskey', TRUE),
('93102750284', 'Samuel', 'McDonald', 'M', 'B4 3BW', 'Birningham', 'Boroughbridge Road', '92', '5', '794413872', 'samuel.mcdonald@gmail.com',NULL, False);

INSERT INTO hdbapp.hospital(idHospital, name)
VALUES
(1,'St.Paul''s Hospital'),
(2,'St.Anthony''s Hospital'),
(3,'St.Mary''s Hospital');

INSERT INTO hdbapp.ward(idWard, name, capacity, idHospital)
VALUES
(1, 'Infectious',10,1),
(2, 'Cardiology',20,1),
(3, 'Neurology',15, 2),
(4, 'Pulmonary', 30, 3);

INSERT INTO hdbapp.medicalCondition(idMedicalCondition, name, isInfectious)
VALUES
(1, 'Covid-19',TRUE),
(2, 'Alzheimer''s disease',FALSE),
(3, 'Hypertension', False);

INSERT INTO hdbapp.doctor(idDoctor, name, surname, gender, tel, email,specialisation, idWard)
VALUES
(66110759354,'Aaliyah','Moran','F', '782835235', 'aaliyah.moran@gmail.com', 'Virusologist',1),
(51042957293,'Alisha', 'Burgess', 'F', '075257190', 'alisha.burges@gmail.com', 'Cardiology',2),
(81011138594, 'Lewis', 'Middleton', 'M', '700659249', 'lewis.middleton@gmail.com', 'Neurologist',3),
(92011894025, 'Luca', 'Parker', 'M', '795714994', 'luca.parker@gmail.com', 'Pulmonologist', 4),
(80071294205, 'Jasmine', 'Dyer', 'F', '509238265', 'jasmine.dyer@gmail.com', 'Virusologist',1);

INSERT INTO hdbapp.disease (idDisease, idPatient, startDate, endDate, idMedicalCondition, idDoctor)
VALUES
(1, '71083086034', '2009-05-11', '2015-09-12', 3, '51042957293'),
(2, '94040472952', '1999-11-24', '2014-02-15', 2, '81011138594'),
(3, '81141105691', '2018-02-02', '2020-06-04', 3, '51042957293'),
(4, '93210524563', '2012-05-03', '2019-07-06', 1, '66110759354'),
(5, '86111174034', '2003-03-17', '2009-04-16', 1, '80071294205'),
(6, '87102589205', '2015-06-17', '2016-02-05', 1, '92011894025'),
(7, '93080583665', '2014-03-02', '2020-07-07', 1, '66110759354'),
(8, '61072586373', '1996-11-05', '2020-11-10', 3, '51042957293'),
(9, '51102609256', '2021-01-01', '2021-01-18', 1, '66110759354'),
(10, '65122058204', '2012-08-10', '2013-06-11',2, '81011138594'),
(11, '87022148571', '2019-08-12', '2021-01-02', 1, '80071294205'),
(12, '93102750284', '1994-02-01', '2014-06-05', 3, '51042957293');

INSERT INTO hdbapp.stay(idStay, idPatient, startDate, EndDate, idDoctor, idWard)
VALUES
(16, '71083086034', '2002-02-01', '2002-03-03', '51042957293', 2),
(15, '94040472952', '2001-01-01', '2001-02-03', '81011138594', 3),
(14, '81141105691', '2002-02-01', '2002-04-04', '51042957293', 2),
(13, '93210524563', '2003-02-02', '2003-05-03', '66110759354', 1),
(12, '86111174034', '2004-03-02', '2004-03-08', '80071294205', 4),
(11, '87102589205', '2005-05-05', '2007-06-06', '92011894025', 1),
(10, '93080583665', '1996-01-01', '2020-07-06', '66110759354', 4),
(9, '61072586373', '2008-10-09', '2008-11-10', '51042957293', 2),
(8, '51102609256', '2019-04-02', '2019-06-04', '66110759354', 1),
(7, '65122058204', '2020-06-02', '2020-09-08', '81011138594', 3),
(6, '87022148571', '2008-02-02', '2008-05-03', '80071294205', 4),
(5, '93102750284', '1995-05-01', '1995-06-06', '51042957293', 2);

INSERT INTO hdbapp.diseaseStay(idDisease,idStay)
VALUES
(1,16),
(2,15),
(3,14),
(4,13),
(5,12),
(6,11),
(7,10),
(8,9),
(9,8),
(10,7),
(11,6),
(12,5);