import sys
from getpass import getpass

import mysql.connector

MYSQL_ERROR_MESSAGES = {
    1036: "I don't know how to write in here, I can only read this table",
    1037: "Server is about to explode, no memory left, restart it",
    1045: "I did not get access with, do I have the correct ID? Check user and pass",
    1049: "For real? That database is not in here. Stop giving me bad directions",
    1051: "There is no such table. Please don't make fun of me",
    2003: "Where is it? I cant find the database on that host",
}


class DatabaseSettings():

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

            TODO: Make it a loop. If connection fails, ask for new
            credentials.

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
