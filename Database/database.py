"""
The class is used to create the database.
"""

import mysql.connector

from Display.display import Display
from glob import Glob

"""
Import mysql.connector Library.

Import different Class.
"""


class MySQL:
    """
    This class is used for the creation, the connection,
    the insertion, the selection of different information
    in the database.
    """

    def __init__(self):
        """
        We build the instance of the class.
        """

        self.display_open_food_fact = Display()

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

        self.category_id = 0

        self.cat_id = 0
        self.food_id = ""
        self.food_name = ""
        self.food_url = ""
        self.food_shop = ""
        self.food_nutrition = ""

        self.substitute_id = 0
        self.substitute_name = ""
        self.substitute_url = ""
        self.substitute_shop = ""
        self.substitute_nutrition = ""

    def create_database(self):
        """
        We are creating the database.
        """

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
                        food_name VARCHAR(250) NOT NULL,\
                        food_url VARCHAR(300) NOT NULL,\
                        food_shop VARCHAR(300),\
                        food_nutrition CHAR(1),\
                        PRIMARY KEY (food_id, cat_id));")
        self.cursor.execute("CREATE TABLE Substitute (\
                substitute_id INT AUTO_INCREMENT NOT NULL,\
                substitute_name VARCHAR(250) NOT NULL,\
                substitute_url VARCHAR(300) NOT NULL,\
                substitute_shop VARCHAR(300),\
                substitute_nutrition CHAR(1),\
                PRIMARY KEY (substitute_id));")

        self.display_open_food_fact.create_database()

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

        self.display_open_food_fact.connection_database()

    def insert_data_category(self, p_category_name):
        """
        Insertion of category information into the database.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        sql = "INSERT INTO Category (category_id, name) VALUES (%s, %s);"
        val = (self.cursor.lastrowid, p_category_name)
        self.cursor.execute(sql, val)

        self.db_connect.commit()

    def insert_data_product(
            self, p_category, p_product_name, p_product_url,
            p_product_shop, p_product_nutrition):
        """
        Insertion of product information into the database.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        sql = "INSERT INTO Food\
         (food_id, cat_id, food_name, food_url, food_shop, food_nutrition)\
         VALUES (%s, %s, %s, %s, %s, %s);"
        val = (
            self.cursor.lastrowid, p_category, p_product_name,
            p_product_url, p_product_shop, p_product_nutrition)
        self.cursor.execute(sql, val)

        self.db_connect.commit()

    def select_category(self):
        """
        We select the category_id column from the Category table
        to retrieve the database information.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        select_category = "SELECT category_id, name FROM Category;"

        self.cursor.execute(select_category)
        for self.category_id, self.name in self.cursor:
            self.display_open_food_fact.select_category_db(
                self.category_id, self.name)

    def select_cat_food(self, p_choice_category):
        """
        In this method we select different columns
        from the Food table. But we also make a join
        between two tables.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        select_cat_food = 'SELECT food_id, food_name FROM Food\
        INNER JOIN Category\
        ON Category.category_id = Food.cat_id\
        WHERE Category.category_id = %s;'

        self.cursor.execute(select_cat_food, p_choice_category)
        for self.food_id, self.food_name in self.cursor:
            self.display_open_food_fact.select_cat_food_db(
                self.food_id, self.food_name)

    def select_food(self, p_choice_product):
        """
        In this method we select different
        columns from the Food table.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        select_food = 'SELECT food_name, food_url, food_shop,' \
                      ' UPPER(food_nutrition) AS food_nutrition_upper FROM Food\
                        WHERE Food.food_id = %s;'

        self.cursor.execute(select_food, p_choice_product)
        for self.food_name, self.food_url, self.food_shop, self.food_nutrition\
                in self.cursor:
            self.display_open_food_fact.select_food_db(
                self.food_name, self.food_url,
                self.food_shop, self.food_nutrition)

    def select_substitute(self, p_choice_category):
        """
        In this method we select different columns
        from the Food table. But we also make a join
        between two tables.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        id_substitute = "1"
        # 102 ==  The letter "f" in ASCII
        nutri_substitute = 102
        substitute = 'SELECT food_id, UPPER(food_nutrition) ' \
                     'AS food_nutrition_upper FROM Food\
                     INNER JOIN Category\
                     ON Category.category_id = Food.cat_id\
                     WHERE Category.category_id = %s;'

        self.cursor.execute(substitute, p_choice_category)
        for self.food_id, self.food_nutrition in self.cursor:
            "print(self.food_id, ord(self.food_nutrition))"
            for increment in range(5):
                """print("increment" + str(increment + 97))"""
                if ord(self.food_nutrition) <= increment + 97 and\
                        ord(self.food_nutrition) < nutri_substitute:
                    id_substitute = self.food_id
                    nutri_substitute = ord(self.food_nutrition)

        select_substitute = 'SELECT food_name, food_url, food_shop, ' \
                            'UPPER(food_nutrition) AS food_nutrition_upper FROM Food\
                            WHERE Food.food_id = %s;'

        self.cursor.execute(select_substitute, (int(id_substitute),))
        for self.food_name, self.food_url, self.food_shop, self.food_nutrition\
                in self.cursor:
            self.display_open_food_fact.select_substitute_db(
                self.food_name, self.food_url,
                self.food_shop, self.food_nutrition)

    def insert_substitute_save(self):
        """
        Insertion of product information into the database.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        sql = "INSERT INTO Substitute " \
              "(substitute_id, substitute_name, substitute_url," \
              " substitute_shop, substitute_nutrition)\
                 VALUES (%s, %s, %s, %s, %s)"
        val = (
            self.cursor.lastrowid, self.food_name,
            self.food_url, self.food_shop, self.food_nutrition)
        self.cursor.execute(sql, val)

        self.db_connect.commit()

    def select_substitute_save(self):
        """
        In this method, we save the selected substitutes.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        select_substitute_save =\
            'SELECT substitute_id, substitute_name FROM Substitute'
        self.cursor.execute(select_substitute_save)
        for self.substitute_id, self.substitute_name in self.cursor:
            self.display_open_food_fact.select_substitute_save_db(
                self.substitute_id, self.substitute_name)

    def information_substitute_save(self, p_choice_substituted):
        """
        In this method, we display the information of the substitutes.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        information_substitute_save = 'SELECT substitute_name,\
        substitute_url, substitute_shop, substitute_nutrition FROM Substitute\
        WHERE Substitute.substitute_id = %s;'

        self.cursor.execute(information_substitute_save, p_choice_substituted)
        for self.substitute_name, self.substitute_url, \
            self.substitute_shop, self.substitute_nutrition\
                in self.cursor:
            self.display_open_food_fact.information_substitute_save_db(
                self.substitute_name, self.substitute_url,
                self.substitute_shop, self.substitute_nutrition)

    def delete_substitute(self, p_choice_delete):
        """
        In this method, we remove the substitutes save.
        """

        self.cursor = self.db_connect.cursor()
        self.cursor.execute("USE `database`;")
        delete_substitute = 'DELETE FROM Substitute\
         WHERE Substitute.substitute_id = %s;'

        self.cursor.execute(delete_substitute, p_choice_delete)
        self.display_open_food_fact.delete_substitute_db(p_choice_delete)

    def data_close(self):
        """
        In this method, we close the database.
        """

        self.cursor = self.db_connect.cursor()
        self.db_connect.commit()
        self.cursor.close()
