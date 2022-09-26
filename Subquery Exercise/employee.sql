CREATE TABLE employee(
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	salary INT
);
INSERT INTO employee(first_name,last_name,salary)
VALUES
	('Tj', 'Olson', 50000),
	('Steven', 'Markle', 30000),
	('Jake', 'The Dog', 3002),
	('Jake', 'The Dog', 3002),
	('Fin', 'The Human', 300002),
	('Alexander', 'The great', 320),
	('Son', 'Goku', 30000),
	('Tj', 'Olsones', 4550000),
	('Steven', 'Markleses', 530000),
	('Jake', 'The Dog 4', 300222),
	('Jake', 'The Dog 3', 3002);
SELECT * FROM employee WHERE salary < 300222;