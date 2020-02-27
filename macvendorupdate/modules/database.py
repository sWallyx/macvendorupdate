from getpass import getpass
import mysql.connector
import sys


class Database():

    def __init__(self):
        self.db_host = None
        self.db_name = None
        self.db_user = None
        self.db_pass = None
        self.conn = None

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
        try:
            conn = mysql.connector.connect(
                host=self.db_host,
                database=self.db_name,
                user=self.db_user,
                password=self.db_pass
            )
        except mysql.connector.Error:
            sys.exit(
                "I am unable to connect to the database, does it really exist."
            )

        return conn
