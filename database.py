import mysql.connector
from constants import MAIN_HOST, MAIN_USER, MAIN_PASSWORD, MAIN_DATABASE, FILE_DATABASE

class Database:

    def connecting(self):

        mydb = mysql.connector.connect(
            host=MAIN_HOST,
            user=MAIN_USER,
            password=MAIN_PASSWORD,
            database=MAIN_DATABASE
        )

    def create_database(self):

        mydb = mysql.connector.connect(
            host=MAIN_HOST,
            user=MAIN_USER,
            password=MAIN_PASSWORD,
        )
        cursor = mydb.cursor()
        sql = open(FILE_DATABASE, "r")
        cursor.execute(sql)