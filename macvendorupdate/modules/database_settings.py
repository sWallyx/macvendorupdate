from getpass import getpass
import mysql.connector
import sys

from global_values import MYSQL_ERROR_MESSAGES

class Database_settings():

    def __init__(self):
        self.db_host = None
        self.db_name = None
        self.db_user = None
        self.db_pass = None

    def ask_for_setup(self):
        """
            Ask for the following DataBase information:
                - Host of the database
                - Database name
                - User
                - Password
        """
        print("Insert the database info")
        self.db_host = input("Host:  ")
        self.db_name = input("Database name:  ")
        self.db_user = input("User:  ")
        self.db_pass = getpass()

    def check_db_connection(self):
        """
            Check if the connection is OK to continue.
            If not shows message and quits.

            TODO: Make it a loop.

            Returns:
                MySQLConnection: Object with the MySQL connection object.
        """
        try:
            conn = mysql.connector.connect(
                host=self.db_host,
                database=self.db_name,
                user=self.db_user,
                password=self.db_pass
            )
        except mysql.connector.Error as err:
            sys.exit(MYSQL_ERROR_MESSAGES[err.errno])


        return conn
