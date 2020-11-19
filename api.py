import mysql.connector
from database import *
import requests
import json

def category():
    emplacement = 0
    category_name = ""
    reponse_json = json.loads(requests.get('https://fr.openfoodfacts.org/langue/francais/categories.json').text)

    'print(reponse_json["tags"][1])'

    print("Sélectionnez la catégorie")

    for data in reponse_json["tags"]:

        emplacement += 1

        if emplacement <= 50:
            print(data["name"] + "->" + str(emplacement))
            category_name = data["name"]
            Database.insert_data_category(category_name)
            
    choice_category = int(input("Tap the category number"))
    food(choice_category, reponse_json)

def food(p_choice_category, p_reponse_json):
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
        product_shop = produit["stores"]
        Database.insert_data_product(product_name, product_url, product_shop)
