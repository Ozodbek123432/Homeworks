#IF NOT EXISTS students;
#DROP TABLE students
#--data bade yaratish buyrug'i
#CREATE TABLE students (
#  id SERIAL,
#  first_name VARCHAR(25),
#  last_name CHAR(25),
#  telephone_number VARCHAR(15),
#  yosh 	INT,
#  kursi CHAR (20)
#);
#
#SELECT *
#FROM students;
#
#INSERT INTO students (first_name, last_name, telephone_number, yosh, kursi) VALUES
#	('oquchi1', 'oquvschi familyasi', '+9989445877551', 14,'bekend 03-25'),
#  	('oquchi2', 'oquvschi familyasi1', '+998844587755',16,'bekend 03-25'),
#	('oquchi3', 'oquvschi familyasi2', '+998944587755',14,'bekend 03-25'),
#  	('oquchi4', 'oquvschi familyasi3', '+998844587755',16,'bekend 03-25');