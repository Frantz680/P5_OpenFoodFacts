"""
The class is used for global variables.
"""

import os

from os.path import join, dirname
from dotenv import load_dotenv

"""
Import os Library.

Import different Class.
"""


class Glob:
    """"
    Global variables.
    """

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    mdp = os.getenv('KEY')

    host = "localhost"
    user = "root"
    password = mdp
    database = "database"
    file_database = "create_db.sql"
    nb_category = 50
