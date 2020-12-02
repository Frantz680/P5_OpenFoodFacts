"""
The class is used for display in the console.
"""

import time


class Display:
    """
    This class is used for displaying the application in the console.
    """

    def __init__(self):
        """
        We build the instance of the class.
        """

        pass

    """
    MENU
    """

    def menu_connection(self):
        """Menu connection."""

        choice = input("\n#### MENU CONNECTION ####\n\n"
              "Press 1 for create database.\n"
              "Press 2 to connect to the existing database.\n"
              "Press 3 for exit.\n")
        return choice

    def menu(self):
        """Menu display."""

        choice = input("\n#### MENU ####\n\n"
              "Press 1 for research substituted.\n"
              "Press 2 for my substituted foods.\n"
              "Press 3 for exit.\n")
        return choice

    def menu_error(self):
        """Error display of number entry for menu."""

        print("Please enter a number between 1-3.\nThank you.")

    def menu_favored(self):
        """Menu favored."""

        choice = input("\n#### FAVORED SUBSTITUTES ####\n\n"
              "Press 1 to see favored substitutes.\n"
              "Press 2 to remove substitutes.\n"
              "Press 3 to return to the menu.\n")
        return choice

    """
    Category and product
    """

    def category(self):
        """Display of categories."""

        print("#### The categories ####\n")

    def choice_category(self):
        """Display choice of categories."""

        choice = (int(input("\nTap the category number.\n")),)
        return choice

    def product(self):
        """Display of products."""

        print("\n#### The products ####\n")

    def choice_product(self):
        """Display choice of products."""

        choice = (int(input("\nTap the product number.\n")),)
        return choice

    def choice_error(self):
        """Display choice error"""

        print("\nTap a number from the list.\nThank you.")

    """
    The substitute
    """

    def suggested_substitute(self):
        """Display of substitute product."""

        print("\nThe suggested substitute for this product is :")

    def substitute_saved(self):
        """Display to record the replacement product."""

        choice = input("\nDo you want to save overrides ?\nPress 1 for yes.\nPress 2 for yes.\n")
        return choice

    def suggested_substitute_error(self):
        """Error display of number entry for substitute."""

        print("Please enter a number between 1-2.\nThank you.\n")

    def favored_substitute(self):
        """Show substitutes save."""

        print("\n### Your substitutes save ###\n")

    def favored_information_substitute(self):
        """Display substitute information select."""

        print("\nSelect your substitute to see the information.")

    def choice_favored_substitute(self):
        """Display choice of favored substitutes."""

        choice = (int(input("\nTap the substitute number.\n")),)
        return choice

    def delete_substitute(self):
        """Show substituted backups to delete."""

        print("\nSelect the substitute to delete.\n")

    def choice_delete_substitute(self):
        """Display the choice of substitutes to delete."""

        choice = (int(input("\nTap the substitute number.\n")),)
        return choice

    """
    API
    """

    def loading_categories(self):
        print("Loading categories into the database.")

    def loading_point_category(self):
        print(".", end="")
        time.sleep(0.009)

    def loading_completed_categories(self):
        print("\nLoading completed.")

    def loading_food(self):
        print("Loading food into the database.")

    def loading_point_food(self):
        print(".", end="")

    def loading_completed_food(self):
        print("\nLoading completed.")

    """
    Database
    """

    def create_database(self):
        print("Creation of the database.")

    def connection_database(self):
        print("Connection to the database.")

    def select_category_db(self, p_category_id, p_name):
        print(str(p_category_id) + "->" + str(p_name))

    def select_cat_food_db(self, p_food_id, p_food_name):
        print(str(p_food_id) + "->" + str(p_food_name))

    def select_food_db(self, p_food_name, p_food_url, p_food_shop, p_food_nutrition):
        print("The product you have selected is:")
        print("\nNAME->" + str(p_food_name) + "\nURL->" + str(p_food_url) + "\nSHOP->" + str(
            p_food_shop) + "\nNUTRI->" + str(p_food_nutrition))

    def select_substitue_db(self, p_food_name, p_food_url, p_food_shop, p_food_nutrition):
        print("\nNAME->" + str(p_food_name) + "\nURL->" + str(p_food_url) + "\nSHOP->" + str(
            p_food_shop) + "\nNUTRI->" + str(p_food_nutrition))

    def select_substitute_save_db(self, p_substitute_id, p_substitute_name):
        print(str(p_substitute_id) + "->" + str(p_substitute_name))

    def information_substitute_save_db(self, p_substitute_name, p_substitute_url, p_substitute_shop, p_substitute_nutrition):
        print("\nNAME->" + str(p_substitute_name) + "\nURL->" + str(p_substitute_url) + "\nSHOP->" + str(
            p_substitute_shop) + "\nNUTRI->" + str(p_substitute_nutrition))

    def delete_substitute_db(self, p_choice_delete):
        print("You have deleted the substitute number: " + str(p_choice_delete[0]))