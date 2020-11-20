from database import *
import requests
import json

class Main():

    def __init__(self):
        self.category_json = json.loads(requests.get('https://fr.openfoodfacts.org/langue/francais/categories.json').text)
        self.database = MySQL()

    def interraction_user(self):
        choice_menu = 1
        self.database.create_database()
        self.database.connecting()

        while choice_menu:

            choice = int(input(
                "Press 1 for research substituted.\n"
                "Press 2 for my substituted foods.\n"
                "Press 3 for exit.\n"
            ))

            if choice == 1:
                print("Sélectionnez la catégorie")
                self.request_category()
                choice_category = int(input("Tap the category number"))
                self.request_food(choice_category, self.category_json)
                choice_food = int(input("Tap the food number"))
                self.request_info_food(choice_food, self.category_json)



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
        emplacement = 0
        category_name = ""

        'print(reponse_json["tags"][1])'

        for data in self.category_json["tags"]:

            emplacement += 1

            if emplacement <= 50:
                print(data["name"] + "->" + str(emplacement))
                category_name = data["name"]
                self.database.insert_data_category(category_name)


    def request_food(self, p_choice_category, p_reponse_json):
        emplacement = 0
        product_name = ""
        product_url = ""
        product_shop = ""

        print("category")
        category_choisi_json = p_reponse_json["tags"][p_choice_category - 1]
        print(category_choisi_json)
        reponse_categeory_json = json.loads(requests.get(category_choisi_json["url"] + ".json").text)
        "print(reponse_categeory_json)"

        for produit in reponse_categeory_json["products"]:
            emplacement += 1

            print(produit["product_name"] + " -> " + str(emplacement))
            product_name = produit["product_name"]
            product_url = produit["url"]
            product_shop = "rien"
            self.database.insert_data_product(product_name, product_url, product_shop)

    def request_info_food(self, p_choice_food, p_reponse_json):
        

def main():

    user = Main()
    user.interraction_user()

if __name__ == '__main__':
    main()