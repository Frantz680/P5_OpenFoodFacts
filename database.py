"""
The class is used to create the database.
"""

import mysql.connector

from glob import Glob

"""
Import from mysql.connector Library.

Import different variables.
"""


class MySQL:
    """
    This class is used for the creation, the connection,
    the insertion, the selection of different information
    in the database.
    """

    def __init__(self):
        """
        We build the constructor.
        """

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
        """
        We are creating the database.
        """

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
                        food_id INT AUTO_INCREMENT NOT NULL,\
                        cat_id INT NOT NULL,\
                        food_name VARCHAR(150) NOT NULL,\
                        food_url VARCHAR(300) NOT NULL,\
                        food_shop VARCHAR(300),\
                        food_nutrition CHAR(1),\
                        PRIMARY KEY (food_id, cat_id));")
        self.cursor.execute("CREATE TABLE Substitute (\
                substitute_id INT AUTO_INCREMENT NOT NULL,\
                substitute_name VARCHAR(150) NOT NULL,\
                substitute_url VARCHAR(300) NOT NULL,\
                substitute_shop VARCHAR(300),\
                substitute_nutrition CHAR(1),\
                PRIMARY KEY (substitute_id));")

        print("Création de la base de donnée")

    def connecting_db(self):
        """
        Connection to the database.
        """
        self.db_connect = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        print("Connection à la base de donnée")

    def insert_data_category(self, p_category_name):
        """
        Insertion of category information into the database.
        """

        self.cursor = self.db_connect.cursor()
        sql = "INSERT INTO Category (category_id, name) VALUES (%s, %s)"
        val = (self.cursor.lastrowid, p_category_name)
        self.cursor.execute(sql, val)

        self.db_connect.commit()

        """print(self.cursor.rowcount, "record inserted.")"""

    def insert_data_product(self, p_category, p_product_name, p_product_url, p_product_shop, p_product_nutrition):
        """
        Insertion of product information into the database.
        """

        self.cursor = self.db_connect.cursor()
        sql = "INSERT INTO Food (food_id, cat_id, food_name, food_url, food_shop, food_nutrition)\
         VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.cursor.lastrowid, p_category, p_product_name, p_product_url, p_product_shop, p_product_nutrition)
        self.cursor.execute(sql, val)

        self.db_connect.commit()

        """print(self.cursor.rowcount, "record inserted.")"""

    def select_category(self):
        """
        We select the category_id column from the Category table
        to retrieve the database information.
        """

        select_category = "SELECT category_id, name FROM Category;"

        self.cursor.execute(select_category)
        for self.category_id, name in self.cursor:
            print(str(self.category_id) + "->" + str(name))

    def select_cat_food(self, p_choice_category):
        """
        In this method we select different columns
        from the Food table. But we also make a join
        between two tables.
        """

        select_cat_food = 'SELECT food_id, food_name FROM Food\
        INNER JOIN Category\
        ON Category.category_id = Food.cat_id\
        WHERE Category.category_id = %s;'

        self.cursor.execute(select_cat_food, p_choice_category)
        for food_id, food_name in self.cursor:
            print(str(food_id) + "->" + str(food_name))

    def select_food(self, p_choice_product):
        """
        In this method we select different
        columns from the Food table.
        """

        select_food = 'SELECT food_name, food_url, food_shop, food_nutrition FROM Food\
        WHERE Food.food_id = %s;'

        self.cursor.execute(select_food, p_choice_product)
        for food_name, food_url, food_shop, food_nutrition in self.cursor:
            print("NAME->" + str(food_name) + "\nURL->" + str(food_url) + "\nSHOP->" + str(food_shop) + "\nNUTRI->" + str(food_nutrition))

    def data_close(self):
        """
        In this method, we close the database.
        """

        self.cursor.close()
        self.db_connect.commit()
