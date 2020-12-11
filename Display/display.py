"""
The class is used for display in the console.
"""

import time

"""
Import time Library.
"""


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

    @staticmethod
    def menu_connection():
        """Menu connection."""

        choice = input("\n#### MENU CONNECTION ####\n\n"
                       "Press 1 for create database.\n"
                       "Press 2 to connect to the existing database.\n"
                       "Press 3 for exit.\n"
                       "Tap the number :")
        return choice

    @staticmethod
    def menu():
        """Menu display."""

        choice = input("\n#### MENU ####\n\n"
                       "Press 1 for research substituted.\n"
                       "Press 2 for my substituted foods.\n"
                       "Press 3 for exit.\n"
                       "Tap the number :")
        return choice

    @staticmethod
    def menu_error():
        """Error display of number entry for menu."""

        print("Please enter a number between 1-3.\nThank you.")

    @staticmethod
    def menu_favored():
        """Menu favored."""

        choice = input("\n#### FAVORED SUBSTITUTES ####\n\n"
                       "Press 1 to see favored substitutes.\n"
                       "Press 2 to remove substitutes.\n"
                       "Press 3 to return to the menu.\n"
                       "Tap the number :")
        return choice

    """
    Category and product
    """

    @staticmethod
    def category():
        """Display of categories."""

        print("#### The categories ####\n")

    @staticmethod
    def choice_category():
        """Display choice of categories."""

        choice = (int(input("\nTap the category number :")),)
        return choice

    @staticmethod
    def product():
        """Display of products."""

        print("\n#### The products ####\n")

    @staticmethod
    def choice_product():
        """Display choice of products."""

        choice = (int(input("\nTap the product number :")),)
        return choice

    @staticmethod
    def choice_error():
        """Display choice error"""

        print("\nTap a number from the list.\nThank you.")

    """
    The substitute
    """

    @staticmethod
    def suggested_substitute():
        """Display of substitute product."""

        print("\nThe suggested substitute for this product is :")

    @staticmethod
    def substitute_saved():
        """Display to record the replacement product."""

        choice = input("\nDo you want to save overrides ?"
                       "\nPress 1 for yes.\nPress 2 for yes.\n"
                       "Tap the number :")
        return choice

    @staticmethod
    def suggested_substitute_error():
        """Error display of number entry for substitute."""

        print("Please enter a number between 1-2.\nThank you.\n")

    @staticmethod
    def favored_substitute():
        """Show substitutes save."""

        print("\n### Your substitutes save ###\n")

    @staticmethod
    def favored_information_substitute():
        """Display substitute information select."""

        print("\nSelect your substitute to see the information.")

    @staticmethod
    def choice_favored_substitute():
        """Display choice of favored substitutes."""

        choice = (int(input("\nTap the substitute number :")),)
        return choice

    @staticmethod
    def delete_substitute():
        """Show substituted backups to delete."""

        print("\nSelect the substitute to delete.\n")

    @staticmethod
    def choice_delete_substitute():
        """Display the choice of substitutes to delete."""

        choice = (int(input("\nTap the substitute number :")),)
        return choice

    """
    API
    """

    @staticmethod
    def loading_categories():
        """Loading categories into the database."""

        print("Loading categories into the database.")

    @staticmethod
    def loading_point_category():
        """Loading categories."""

        print(".", end="")
        time.sleep(0.009)

    @staticmethod
    def loading_completed_categories():
        """Loading completed categories."""

        print("\nLoading completed.")

    @staticmethod
    def loading_food():
        """Loading food into the database."""

        print("Loading food into the database.")

    @staticmethod
    def loading_point_food():
        """Loading food."""

        print(".", end="")

    @staticmethod
    def loading_completed_food():
        """Loading completed food."""

        print("\nLoading completed.")

    """
    Database
    """

    @staticmethod
    def create_database():
        """Creation of the database."""

        print("Creation of the database.")

    @staticmethod
    def connection_database():
        """Connection to the database."""

        print("Connection to the database.")

    @staticmethod
    def select_category_db(p_category_id, p_name):
        """Category displays."""

        print(str(p_category_id) + "->" + str(p_name))

    @staticmethod
    def select_cat_food_db(p_food_id, p_food_name):
        """Product displays."""

        print(str(p_food_id) + "->" + str(p_food_name))

    @staticmethod
    def select_food_db(
            p_food_name, p_food_url,
            p_food_shop, p_food_nutri):
        """Product display select."""

        print("The product you have selected is:")
        print("\nNAME->" + str(p_food_name) + "\nURL->" + str(p_food_url))
        print("\nSHOP->" + str(p_food_shop) + "\nNUTRI->" + str(p_food_nutri))

    @staticmethod
    def select_substitute_db(
            p_food_name, p_food_url,
            p_food_shop, p_food_nutri):
        """Substitute display select."""

        print("\nNAME->" + str(p_food_name) + "\nURL->" + str(p_food_url))
        print("\nSHOP->" + str(p_food_shop) + "\nNUTRI->" + str(p_food_nutri))

    @staticmethod
    def select_substitute_save_db(p_substitute_id, p_substitute_name):
        """Display of substitutes save."""

        print(str(p_substitute_id) + "->" + str(p_substitute_name))

    @staticmethod
    def information_substitute_save_db(
            p_substitute_name, p_substitute_url,
            p_substitute_shop, p_substitute_nutrition):
        """Display information about the substitute select."""

        print("\nNAME->" + str(p_substitute_name)
              + "\nURL->" + str(p_substitute_url))
        print("\nSHOP->" + str(p_substitute_shop)
              + "\nNUTRI->" + str(p_substitute_nutrition))

    @staticmethod
    def delete_substitute_db(p_choice_delete):
        """Display of the substitute number delete."""

        print("You have deleted the substitute number: " +
              str(p_choice_delete[0]))
