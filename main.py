import mysql.connector
from api import *
from database import *

class Main():

    def __init__(self):
        pass


    def connecting(self):
        data = Database()
        data.create_database()
        "data.connecting()"
        choice_menu = 1

        while choice_menu:

            choice = int(input(
                "Press 1 for research substituted.\n"
                "Press 2 for my substituted foods.\n"
                "Press 3 for exit.\n"
            ))

            if choice == 1:
                category()

            elif choice == 2:
                self.my_substituted()


            elif choice == 3:
                data.data_close()
                choice_menu = 0


    def my_substituted(self):
        choice_substituted = 1

        while choice_substituted:

            choice = int(input(
                "Press 1 to see favored substitutes.\n"
                "Press 2 to remove substitutes.\n"
                "Press 3 to return to the menu.\n"
            ))

            if choice == 1:
                print("favori")

            if choice == 2:
                print("sup")

            if choice == 3:
                self.connecting()

def main():
    reception = Main()
    reception.connecting()


if __name__ == '__main__':
    main()
