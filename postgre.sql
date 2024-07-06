CREATE DATABASE aiexcel;

CREATE USER rupeshsigdel WITH PASSWORD 'rupesh@123';
ALTER ROLE rupeshsigdel SET client_encoding TO 'utf8';
ALTER ROLE rupeshsigdel SET default_transaction_isolation TO 'read committed';
ALTER ROLE rupeshsigdel SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE aiexcel TO rupeshsigdel;

\c aiexcel

CREATE TABLE excel_knowledge (
    id SERIAL PRIMARY KEY,
    category VARCHAR(50),
    question TEXT,
    answer TEXT
);

INSERT INTO excel_knowledge (category, question, answer) VALUES
('Formula', 'What is VLOOKUP?', 'The VLOOKUP function searches for a value in the first column of a table and returns a value in the same row from a column you specify.'),
('Rule', 'How to use IF function?', 'The IF function checks whether a condition is met and returns one value for TRUE and another for FALSE.'),
('Syntax', 'What is the syntax for SUM?', 'The SUM function syntax is SUM(number1, [number2], ...).'),
('Project Idea', 'Can you suggest a project for economics?', 'Create a financial forecasting model using regression analysis.');

SELECT pg_reload_conf();
