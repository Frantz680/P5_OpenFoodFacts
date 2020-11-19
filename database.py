import mysql.connector

from glob import *

class Database:
    
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
        cursor = mydb.cursor()
        sql = open(Glob.file_database).read()
        cursor.execute(sql, multi=True)

        mydb.commit()

        print(cursor.rowcount, "ok")


    def insert_data_category(p_category_name):

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

    def insert_data_product(p_product_name, p_product_url, p_product_shop):
        mydb = mysql.connector.connect(
            host=Glob.host,
            user=Glob.user,
            password=Glob.password,
            database=Glob.database
        )
        cursor = mydb.cursor()
        sql = "INSERT INTO Food (id, category_id, food_name, food_url, food_shop) VALUES (%s, %s, %s, %s, %s)"
        val = (cursor.lastrowid, cursor.lastrowid, p_product_name, p_product_url, p_product_shop)
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
