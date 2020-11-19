DROP DATABASE IF EXISTS `database`;
CREATE DATABASE IF NOT EXISTS `database`;
USE `database`;

CREATE TABLE Category (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(250) NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE Food (
                id INT AUTO_INCREMENT NOT NULL,
                category_id INT AUTO_INCREMENT NOT NULL,
                food_name VARCHAR(150) NOT NULL,
                food_url VARCHAR(300) NOT NULL,
                food_shop VARCHAR(300),
                PRIMARY KEY (id)
);


CREATE TABLE Substitute (
                id INT AUTO_INCREMENT NOT NULL,
                id_food VARCHAR AUTO_INCREMENT NOT NULL,
                substitute_name VARCHAR(150) NOT NULL,
                substitute_url VARCHAR(300) NOT NULL,
                substitute_shop VARCHAR(300),
                PRIMARY KEY (id, id_food)
);


ALTER TABLE Food ADD CONSTRAINT category_product_fk
FOREIGN KEY (id)
REFERENCES Category (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE Substitute ADD CONSTRAINT product_substitute_fk
FOREIGN KEY (id)
REFERENCES Food (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;