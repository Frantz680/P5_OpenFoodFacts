import mysql.connector

from glob import *


class MySQL:

    def __init__(self):
        self.host = Glob.host
        self.user = Glob.user
        self.password = Glob.password
        self.database = Glob.database
        self.db_connect = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        self.cursor = self.db_connect.cursor()


    def create_database(self):

        """sql = open(Glob.file_database, 'r')
        sql2 = " ".join(sql.readlines())
        cursor.execute(sql2, multi=True)"""

        self.cursor.execute("DROP DATABASE IF EXISTS `database`;")
        self.cursor.execute("CREATE DATABASE `database`;")
        self.cursor.execute("USE `database`;")
        self.cursor.execute("CREATE TABLE Category (\
                        category_id INT AUTO_INCREMENT NOT NULL,\
                        name VARCHAR(250) NOT NULL,\
                        PRIMARY KEY (category_id));")
        self.cursor.execute("CREATE TABLE Food (\
                        id INT AUTO_INCREMENT NOT NULL,\
                        category_id INT NOT NULL,\
                        food_name VARCHAR(150) NOT NULL,\
                        food_url VARCHAR(300) NOT NULL,\
                        food_shop VARCHAR(300),\
                        PRIMARY KEY (id, category_id));")
        self.cursor.execute("CREATE TABLE Substitute (\
                id INT AUTO_INCREMENT NOT NULL,\
                substitute_name VARCHAR(150) NOT NULL,\
                substitute_url VARCHAR(300) NOT NULL,\
                substitute_shop VARCHAR(300),\
                PRIMARY KEY (id));")
        print("Création de la base de donnée")

    def connecting_db(self):
        print("Connection à la base de donnée")
        self.db_connect = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def insert_data_category(self, p_category_name):

        self.cursor = self.db_connect.cursor()
        sql = "INSERT INTO Category (category_id, name) VALUES (%s, %s)"
        val = (self.cursor.lastrowid, p_category_name)
        self.cursor.execute(sql, val)

        self.db_connect.commit()

        """print(self.cursor.rowcount, "record inserted.")"""

    def insert_data_product(self, p_category, p_product_name, p_product_url, p_product_shop):

        self.cursor = self.db_connect.cursor()
        sql = "INSERT INTO Food (id, category_id, food_name, food_url, food_shop) VALUES (%s, %s, %s, %s, %s)"
        val = (self.cursor.lastrowid, p_category, p_product_name, p_product_url, p_product_shop)
        self.cursor.execute(sql, val)

        self.db_connect.commit()

        """print(self.cursor.rowcount, "record inserted.")"""

    def select_category(self):
        select_category = "SELECT name FROM Category;"
        self.cursor.execute(select_category)
        for name in self.cursor:
            print(name)

    def data_close(self):

        self.cursor.close()
        self.db_connect.commit()
