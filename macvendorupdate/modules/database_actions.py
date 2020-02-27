import mysql.connector


class Database_actions():
    """
        Object to hold all the actions that the database will
        need to do.
    """

    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def execute_query(self, sql_query):
        """
            Executes the given sql query into the logged
            database.

            Args:
                sql_query {str}: SQL query string
        """
        try:
            self.cur.execute(sql_query)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

    def close_database(self):
        """
            Ends the conexion with the database
        """
        self.cur.close()
        self.conn.close()
