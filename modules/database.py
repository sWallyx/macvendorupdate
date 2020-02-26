from getpass import getpass

class Database():

    def __init__(self):
        self.db_host = None
        self.db_name = None
        self.db_user = None
        self.db_pass = None

    def ask_for_setup(self):
        print("Insert the database info")
        self.db_host = input("Host:  ")
        self.db_name = input("Database name:  ")
        self.db_user = input("User:  ")
        self.db_pass = getpass()
