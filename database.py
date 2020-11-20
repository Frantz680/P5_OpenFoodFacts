import mysql.connector

from glob import *


class MySQL:

    def __init__(self):
        pass

    def connecting(self):
        mydb = mysql.connector.connect(
            host=Glob.host,
            user=Glob.user,
            password=Glob.password,
            database=Glob.database
        )

    def create_database(self):
        mydb = mysql.connector.connect(
            host=Glob.host,
            user=Glob.user,
            password=Glob.password
        )
        print(mydb)
        cursor = mydb.cursor()
        """sql = open(Glob.file_database, 'r')
        sql2 = " ".join(sql.readlines())
        cursor.execute(sql2, multi=True)"""

        cursor.execute("DROP DATABASE IF EXISTS `database`;")
        cursor.execute("CREATE DATABASE `database`;")
        cursor.execute("USE `database`;")
        cursor.execute("CREATE TABLE Category (\
                        id INT AUTO_INCREMENT NOT NULL,\
                        name VARCHAR(250) NOT NULL,\
                        PRIMARY KEY (id));")
        cursor.execute("CREATE TABLE Food (\
                        id INT AUTO_INCREMENT NOT NULL,\
                        food_name VARCHAR(150) NOT NULL,\
                        food_url VARCHAR(300) NOT NULL,\
                        food_shop VARCHAR(300),\
                        PRIMARY KEY (id));")
        cursor.execute("CREATE TABLE Substitute (\
                id INT AUTO_INCREMENT NOT NULL,\
                substitute_name VARCHAR(150) NOT NULL,\
                substitute_url VARCHAR(300) NOT NULL,\
                substitute_shop VARCHAR(300),\
                PRIMARY KEY (id));")

        print(cursor.rowcount, "ok")

    def insert_data_category(self, p_category_name):
        mydb = mysql.connector.connect(
            host=Glob.host,
            user=Glob.user,
            password=Glob.password,
            database=Glob.database
        )

        cursor = mydb.cursor()
        sql = "INSERT INTO Category (id, name) VALUES (%s, %s)"
        val = (cursor.lastrowid, p_category_name)
        cursor.execute(sql, val)

        mydb.commit()

        print(cursor.rowcount, "record inserted.")

    def insert_data_product(self, p_product_name, p_product_url, p_product_shop):
        mydb = mysql.connector.connect(
            host=Glob.host,
            user=Glob.user,
            password=Glob.password,
            database=Glob.database
        )
        cursor = mydb.cursor()
        sql = "INSERT INTO Food (id, food_name, food_url, food_shop) VALUES (%s, %s, %s, %s)"
        val = (cursor.lastrowid, p_product_name, p_product_url, p_product_shop)
        cursor.execute(sql, val)

        mydb.commit()

        print(cursor.rowcount, "record inserted.")

    def data_close(self):
        mydb = mysql.connector.connect(
            host=Glob.host,
            user=Glob.user,
            password=Glob.password,
            database=Glob.database
        )
        cursor = mydb.cursor()
        cursor.close()
        mydb.commit()
