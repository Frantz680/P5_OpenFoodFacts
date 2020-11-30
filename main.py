"""
Application "Pur Beurre" for healthier eating.
"""

from api import Api
from database import MySQL
from display import Display

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
        self.database.create_database()
        self.database.connecting_db()

        self.api_open_food_fact = Api()
        self.api_open_food_fact.request_category()
        self.api_open_food_fact.request_food()

        self.display_open_food_fact = Display()

    def interraction_user(self):
        """
        This method allows you to search for the products to substitutes
        and the preferred substitutes.
        """

        choice_menu = 1

        while choice_menu:

            choice = input(self.display_open_food_fact.menu())

            if choice == "1":
                self.display_open_food_fact.category()
                self.database.select_category()

                # (input(),) to make a tuple
                choice_category = (input(self.display_open_food_fact.choice_category()),)
                self.display_open_food_fact.product()
                self.database.select_cat_food(choice_category)

                choice_product = (input(self.display_open_food_fact.choice_product()),)
                self.database.select_food(choice_product)

                self.display_open_food_fact.suggested_substitute()
                self.database.select_substitue(choice_category)

                saved = input(self.display_open_food_fact.substitute_saved())

                if saved == "1":
                    self.database.insert_substitute_save()

                elif saved == "2":
                    pass
                else:
                    self.display_open_food_fact.suggested_substitute_error()

            elif choice == "2":
                self.my_substituted()

            elif choice == "3":
                self.database.data_close()
                choice_menu = 0

            else:
                self.display_open_food_fact.menu_error()

    def my_substituted(self):
        """
        This method allows you to see the favorite substitutes and delete them.
        """

        substituted = 1

        while substituted:

            choice = input(self.display_open_food_fact.menu_favored())

            if choice == "1":
                self.display_open_food_fact.favored_substitute()
                self.database.select_substitute_save()

                self.display_open_food_fact.favored_information_substitute()
                choice_substituted = (input(self.display_open_food_fact.choice_favored_substitute()),)
                self.database.information_substitute_save(choice_substituted)

            elif choice == "2":
                self.display_open_food_fact.delete_substitute()
                self.database.select_substitute_save()

                choice_delete = (input(self.display_open_food_fact.choice_delete_substitute()),)
                self.database.delete_substitute(choice_delete)

            elif choice == "3":
                self.interraction_user()

            else:
                self.display_open_food_fact.menu_error()


def main():
    """
    Function
    """

    user = Main()
    user.interraction_user()


"""
The main program
"""

if __name__ == '__main__':
    main()
