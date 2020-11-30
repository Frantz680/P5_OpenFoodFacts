"""
Application "Pur Beurre" for healthier eating.
"""

from api import Api
from database import MySQL

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

    def interraction_user(self):
        """
        This method allows you to search for the products to substitutes
        and the preferred substitutes.
        """

        choice_menu = 1

        while choice_menu:

            choice = input(
                "\n#### MENU ####\n\n"
                "Press 1 for research substituted.\n"
                "Press 2 for my substituted foods.\n"
                "Press 3 for exit.\n"
            )

            if choice == "1":
                print("#### The categories ####\n")
                self.database.select_category()

                # (input(),) to make a tuple
                choice_category = (input("\nTap the category number.\n"),)
                print("\n#### The products ####\n")
                self.database.select_cat_food(choice_category)

                choice_product = (input("\nTap the product number.\n"),)
                self.database.select_food(choice_product)

                print("\nThe suggested substitute for this product is :")
                self.database.select_substitue(choice_category)

                saved = input("\nDo you want to save overrides ?\nPress 1 for yes.\nPress 2 for yes.\n")

                if saved == "1":
                    self.database.insert_substitute_save()

                elif saved == "2":
                    pass
                else:
                    print("Please enter a number between 1-2.\nThank you.\n")

            elif choice == "2":
                self.my_substituted()

            elif choice == "3":
                self.database.data_close()
                choice_menu = 0

            else:
                print("Please enter a number between 1-3.\nThank you.")

    def my_substituted(self):
        """
        This method allows you to see the favorite substitutes and delete them.
        """

        substituted = 1

        while substituted:

            choice = input(
                "\n#### FAVORED SUBSTITUTES ####\n\n"
                "Press 1 to see favored substitutes.\n"
                "Press 2 to remove substitutes.\n"
                "Press 3 to return to the menu.\n"
            )

            if choice == "1":
                print("### Your substitutes save ###")
                self.database.select_substitute_save()

                print("Select your substitute to see the information.\n")
                choice_substituted = (input("\nTap the substitute number.\n"),)
                self.database.information_substitute_save(choice_substituted)

            elif choice == "2":
                print("\nSelect the substitute to delete.\n")
                self.database.select_substitute_save()

                choice_delete = (input("\nTap the substitute number.\n"),)
                self.database.delete_substitute(choice_delete)

            elif choice == "3":
                self.interraction_user()

            else:
                print("Please enter a number between 1-3.\nThank you.")


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
