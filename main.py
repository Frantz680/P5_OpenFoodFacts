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
                "Press 1 for research substituted.\n"
                "Press 2 for my substituted foods.\n"
                "Press 3 for exit.\n"
            )

            if choice == "1":
                print("Sélectionnez la catégorie")
                self.database.select_category()

                choice_category = (input("Tap the category number"),)# (int(input()),) pour faire un tuple
                self.database.select_cat_food(choice_category)

                choice_product = (input("Tap the product number"),)
                self.database.select_food(choice_product)

                print("Le substitue proposer pour ce produit est :")
                self.database.select_substitue(choice_category)

                saved = input("Voulez vous sauvegardez ce substitue ?\nTapez 1 pour oui.\nTapez 2 pour non.\n")

                if saved == "1":
                    self.database.insert_substitute_save()

                elif saved == "2":
                    pass
                else:
                    print("Please enter a number between 1-2.\nThank you.")

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
                "Press 1 to see favored substitutes.\n"
                "Press 2 to remove substitutes.\n"
                "Press 3 to return to the menu.\n"
            )

            if choice == "1":
                print("Selectionnez votre substitue pour voir les information.")
                self.database.select_substitute_save()

                choice_substituted = (input("Tap the substitute number.\n"),)
                self.database.information_substitute_save(choice_substituted)

            elif choice == "2":
                print("Selectionnez le substitue à supprimer.")
                self.database.select_substitute_save()

                choice_delete = (input("Tap the substitute number.\n"),)
                self.database.delete_substitute(choice_delete)

            elif choice == "3":
                self.interraction_user()

            else:
                print("Please enter a number between 1-3.\nThank you.")


    def request_category(self):
        """
        Get category names from Open Food Facts.
        """

        print("Chargement des catégories dans la database")

        for compteur in range(Glob.nb_category):
            self.database.insert_data_category(self.category_json["tags"][compteur]["name"])
            print(".", end="")
            time.sleep(0.009)

        print("\nChargement terminée")

    def request_food(self):
        """
        Get product information from Open Food Facts.
        """

        emplacement = 0
        product_name = ""
        product_url = ""
        product_shop = ""
        product_nutrition = ""

        print("Chargement des aliments dans la database")

        for category in range(Glob.nb_category):
            category_choisi_json = self.category_json["tags"][category - 1]
            "print(category_choisi_json)"

            reponse_categeory_json = json.loads(requests.get(category_choisi_json["url"] + ".json").text)
            "print(reponse_categeory_json)"

            for produit in reponse_categeory_json["products"]:
                emplacement += 1

                """print(produit["product_name"] + " -> " + str(emplacement))"""

                product_name = produit["product_name"]

                product_url = produit["url"]

                try:
                    product_shop = produit["stores"]
                except KeyError:
                    pass

                try:
                    product_nutrition = produit["nutrition_grades"]
                except KeyError:
                    pass

                self.database.insert_data_product(category, product_name, product_url, product_shop, product_nutrition)

            print(".", end="")

        print("\nChargement terminée")


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
