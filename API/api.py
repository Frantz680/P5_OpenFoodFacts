"""
The class is used for the API.
"""

import requests
import json

from Display.display import Display
from Database.database import MySQL
from glob import Glob

"""
Import from requests, json Library.

Import different class.
"""


class Api:
    """
    This
    class is used for information retrieval in the API.
    """

    def __init__(self):
        """
        We build the instance of the class.
        """
        self.database = MySQL()

        self.url = \
            'https://fr.openfoodfacts.org/langue/francais/categories.json'

        self.category_json = json.loads(requests.get(self.url).text)

        self.display_open_food_fact = Display()

    def request_category(self):
        """
        Get category names from Open Food Facts.
        """

        self.display_open_food_fact.loading_categories()

        for counter in range(Glob.nb_category):
            self.database.insert_data_category(
                self.category_json["tags"][counter]["name"])
            self.display_open_food_fact.loading_point_category()

        self.display_open_food_fact.loading_completed_categories()

    def request_food(self):
        """
        Get product information from Open Food Facts.
        """

        "emplacement = 0"
        product_name = ""
        product_url = ""
        product_shop = ""
        product_nutrition = ""

        self.display_open_food_fact.loading_food()

        for category in range(Glob.nb_category + 1):
            category_choice_json = self.category_json["tags"][category - 1]
            "print(category_choisi_json)"

            answer_category_json = json.loads(
                requests.get(category_choice_json["url"] + ".json").text)
            "print(answer_category_json)"

            for product in answer_category_json["products"]:
                "emplacement += 1"

                """print(produit["product_name"]
                 + " -> " + str(emplacement))
                 """

                try:
                    product_name = product["product_name"]
                except KeyError:
                    pass

                try:
                    product_url = product["url"]
                except KeyError:
                    pass

                try:
                    product_shop = product["stores"]
                except KeyError:
                    pass

                try:
                    product_nutrition = product["nutrition_grades"]
                except KeyError:
                    pass

                self.database.insert_data_product(
                    category, product_name,
                    product_url, product_shop, product_nutrition)

            self.display_open_food_fact.loading_point_food()

        self.display_open_food_fact.loading_completed_food()
