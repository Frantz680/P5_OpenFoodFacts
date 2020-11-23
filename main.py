from database import *
import time
import requests
import json

class Main():

    def __init__(self):
        self.category_json = json.loads(requests.get('https://fr.openfoodfacts.org/langue/francais/categories.json').text)
        self.database = MySQL()
        self.database.create_database()
        self.database.connecting_db()
        self.request_category()
        self.request_food()

    def interraction_user(self):
        choice_menu = 1

        while choice_menu:

            choice = int(input(
                "Press 1 for research substituted.\n"
                "Press 2 for my substituted foods.\n"
                "Press 3 for exit.\n"
            ))

            if choice == 1:
                print("Sélectionnez la catégorie")
                self.database.select_category()

                choice_category = (int(input("Tap the category number")),)
                self.database.select_cat_food(choice_category)

                choice_product = (int(input("Tap the product number")),)
                self.database.select_food(choice_product)

                print("Le substitue proposer pour ce produit est :")
                "self.database.substitue()"


            elif choice == 2:
                self.my_substituted()


            elif choice == 3:
                self.database.data_close()
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
                self.interraction_user()

    def request_category(self):

        print("Chargement des catégories dans la database")
        for compteur in range(Glob.nb_category):
            self.database.insert_data_category(self.category_json["tags"][compteur]["name"])
            print(".", end="")
            time.sleep(0.009)
        print("\nChargement terminée")

    def request_food(self):
        emplacement = 0
        product_name = ""
        product_url = ""
        product_shop = ""
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
                product_shop = ""
                self.database.insert_data_product(category, product_name, product_url, product_shop)
            print(".", end="")
        print("\nChargement terminée")


def main():

    user = Main()
    user.interraction_user()

if __name__ == '__main__':
    main()