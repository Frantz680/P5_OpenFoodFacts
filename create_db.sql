DROP DATABASE IF EXISTS `datatest`;
CREATE DATABASE IF NOT EXISTS `datatest`;
USE `datatest`;



CREATE TABLE Category (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(150) NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE Product (
                id INT NOT NULL,
                name VARCHAR(150) NOT NULL,
                description VARCHAR(1000),
                PRIMARY KEY (id)
);


CREATE TABLE Substitute (
                id INT NOT NULL,
                name VARCHAR(150) NOT NULL,
                nutritional_information CHAR(1),
                organic BOOLEAN,
                description VARCHAR(1000),
                PRIMARY KEY (id)
);


CREATE TABLE Shop (
                id INT NOT NULL,
                name VARCHAR(150) NOT NULL,
                description VARCHAR(1000),
                website VARCHAR(250),
                PRIMARY KEY (id)
);


ALTER TABLE Product ADD CONSTRAINT category_product_fk
FOREIGN KEY (id)
REFERENCES Category (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE Substitute ADD CONSTRAINT product_substitute_fk
FOREIGN KEY (id)
REFERENCES Product (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE Shop ADD CONSTRAINT substitute_shop_fk
FOREIGN KEY (id)
REFERENCES Substitute (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
