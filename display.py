"""
The class is used for display in the console.
"""


class Display:
    """
    This class is used for displaying the application in the console.
    """

    def __init__(self):
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
