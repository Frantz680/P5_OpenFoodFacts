"""
The class is used for display in the console.
"""


class Display:
    """
    This class is used for displaying the application in the console.
    """

    def menu(self):
        """Menu display."""

        print("\n#### MENU ####\n\n"
        "Press 1 for research substituted.\n"
        "Press 2 for my substituted foods.\n"
        "Press 3 for exit.\n")

    def category(self):
        """Display of categories."""

        print("#### The categories ####\n")

    def choice_category(self):
        """Display choice of categories."""

        print("\nTap the category number.\n")

    def product(self):
        """Display of products."""

        print("\n#### The products ####\n")

    def choice_product(self):
        """Display choice of products."""

        print("\nTap the product number.\n")

    def suggested_substitute(self):
        """Display of substitute product."""

        print("\nThe suggested substitute for this product is :")

    def substitute_saved(self):
        """Display to record the replacement product."""

        print("\nDo you want to save overrides ?\nPress 1 for yes.\nPress 2 for yes.\n")

    def suggested_substitute_error(self):
        """Error display of number entry for substitute."""

        print("Please enter a number between 1-2.\nThank you.\n")

    def menu_error(self):
        """Error display of number entry for menu."""

        print("Please enter a number between 1-3.\nThank you.")

    def menu_favored(self):
        """Menu favored."""

        print("\n#### FAVORED SUBSTITUTES ####\n\n"
              "Press 1 to see favored substitutes.\n"
              "Press 2 to remove substitutes.\n"
              "Press 3 to return to the menu.\n")

    def favored_substitute(self):
        """Show substitutes save."""

        print("### Your substitutes save ###")

    def favored_information_substitute(self):
        """Display substitute information select."""

        print("Select your substitute to see the information.\n")

    def choice_favored_substitute(self):
        """Display choice of favored substitutes."""

        print("\nTap the substitute number.\n")

    def delete_substitute(self):
        """Show substituted backups to delete."""

        print("\nSelect the substitute to delete.\n")

    def choice_delete_substitute(self):
        """Display the choice of substitutes to delete."""

        print("\nTap the substitute number.\n")