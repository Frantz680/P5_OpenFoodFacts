"""
Application "Pur Beurre" for healthier eating.
"""

import time
import requests
import json

from glob import Glob
from database import MySQL

"""
Import from time, requests, json Library.

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

        self.category_json = json.loads\
            (requests.get('https://fr.openfoodfacts.org/langue/francais/categories.json').text)
        self.database = MySQL()
        self.database.create_database()
        self.database.connecting_db()
        self.request_category()
        self.request_food()

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

    def request_category(self):
        """
        Get category names from Open Food Facts.
        """

        print("Loading categories into the database.")

        for counter in range(Glob.nb_category):
            self.database.insert_data_category(self.category_json["tags"][counter]["name"])
            print(".", end="")
            time.sleep(0.009)

        print("\nLoading completed.")

    def request_food(self):
        """
        Get product information from Open Food Facts.
        """

        "emplacement = 0"
        product_name = ""
        product_url = ""
        product_shop = ""
        product_nutrition = ""

        print("Loading food into the database.")

        for category in range(Glob.nb_category):
            category_choice_json = self.category_json["tags"][category - 1]
            "print(category_choisi_json)"

            answer_category_json = json.loads(requests.get(category_choice_json["url"] + ".json").text)
            "print(answer_category_json)"

            for product in answer_category_json["products"]:
                "emplacement += 1"

                """print(produit["product_name"] + " -> " + str(emplacement))"""

                product_name = product["product_name"]

                product_url = product["url"]

                try:
                    product_shop = product["stores"]
                except KeyError:
                    pass

                try:
                    product_nutrition = product["nutrition_grades"]
                except KeyError:
                    pass

                self.database.insert_data_product(category, product_name, product_url, product_shop, product_nutrition)

            print(".", end="")

        print("\nLoading completed.")


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
