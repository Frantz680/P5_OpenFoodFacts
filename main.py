"""
Application "Pur Beurre" for healthier eating.
"""

from api import Api
from database import MySQL
from display import Display
from glob import Glob

"""
Import different class.
"""


class Main:
    """
    This class is used for the
    application menu and the different requests.
    """

    def __init__(self):
        """
        We build the constructor.
        """

        self.database = MySQL()

        self.api_open_food_fact = Api()

        self.display_open_food_fact = Display()

    def interaction_user_connect(self):

        choice_connection = 1

        while choice_connection:
            choice_connec = input(self.display_open_food_fact.menu_connection())

            if choice_connec == "1":
                self.database.create_database()
                self.database.connecting_db()
                self.api_open_food_fact.request_category()
                self.api_open_food_fact.request_food()
                self.interaction_user()
                break

            elif choice_connec == "2":
                self.database.connecting_db()
                self.interaction_user()
                break

            elif choice_connec == "3":
                choice_connection = 0

            else:
                self.display_open_food_fact.menu_error()

    def interaction_user(self):
        """
        This method allows you to search for the products to substitutes
        and the preferred substitutes.
        """

        choice_menu = 1

        while choice_menu:

            choice = input(self.display_open_food_fact.menu())

            if choice == "1":
                while True:

                    self.display_open_food_fact.category()
                    self.database.select_category()

                    try:
                        choice_category = (int(input(self.display_open_food_fact.choice_category())),)

                        if choice_category[0] <= Glob.nb_category:
                            print(choice_category[0])
                            break

                        else:
                            print(choice_category[0])
                            self.display_open_food_fact.choice_error()

                    except ValueError:
                        self.display_open_food_fact.choice_error()

                while True:
                    try:
                        self.display_open_food_fact.product()
                        self.database.select_cat_food(choice_category)
                        choice_product = (int(input(self.display_open_food_fact.choice_product())),)
                        self.database.select_food(choice_product)
                        break

                    except ValueError:
                        self.display_open_food_fact.choice_error()

                while True:

                    self.display_open_food_fact.suggested_substitute()
                    self.database.select_substitue(choice_category)
                    saved = input(self.display_open_food_fact.substitute_saved())

                    if saved == "1":
                        self.database.insert_substitute_save()
                        break

                    elif saved == "2":
                        break
                    else:
                        self.display_open_food_fact.suggested_substitute_error()

            elif choice == "2":
                self.favored_substitutes()

            elif choice == "3":
                self.database.data_close()
                break

            else:
                self.display_open_food_fact.menu_error()

    def favored_substitutes(self):
        """
        This method allows you to see the favorite substitutes and delete them.
        """

        substituted = 1

        while substituted:

            choice = input(self.display_open_food_fact.menu_favored())

            if choice == "1":
                self.display_open_food_fact.favored_substitute()

                while True:
                    try:
                        self.database.select_substitute_save()
                        self.display_open_food_fact.favored_information_substitute()
                        choice_substituted = (int(input(self.display_open_food_fact.choice_favored_substitute())),)
                        self.database.information_substitute_save(choice_substituted)
                        break

                    except ValueError:
                        self.display_open_food_fact.choice_error()

            elif choice == "2":
                while True:
                    try:
                        self.display_open_food_fact.delete_substitute()
                        self.database.select_substitute_save()
                        choice_delete = (int(input(self.display_open_food_fact.choice_delete_substitute())),)
                        self.database.delete_substitute(choice_delete)
                        break

                    except ValueError:
                        self.display_open_food_fact.choice_error()

            elif choice == "3":
                substituted = 0
                self.interaction_user()

            else:
                self.display_open_food_fact.menu_error()


def main():
    """
    Function
    """

    user = Main()
    user.interaction_user_connect()


"""
The main program
"""

if __name__ == '__main__':
    main()
