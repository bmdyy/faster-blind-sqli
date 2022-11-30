/*
William Moody (@bmdyy)
30.11.2022
*/

DROP DATABASE IF EXISTS fbsqli;
CREATE DATABASE fbsqli;
USE fbsqli;
CREATE TABLE users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(72) NOT NULL,
    email VARCHAR(30) NOT NULL
);
INSERT INTO users (username, password, email) VALUES ('bmdyy', '$2a$12$HEXnjRPQxxSLVrdUSf7d6.uHn2LZt4vyZ2CN66L/qI177ovoHea66', 'bmdyy@evil.com');