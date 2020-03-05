import re

from modules.database_settings import Database_settings
from modules.database_actions import Database_actions
from misc_functions import (
    downloadFile,
    getValuesFromLine,
    strip_and_concat,
    end_steps
)

from global_values import OUI_FILE, OUI_URL


def updateMysql():
    """
        Writes the info from the file into the MySQL table.

        NOTE: Read README.md to know the needed table structure
    """
    # create database_config object
    database_config = Database_settings()

    # ask for database config
    database_config.ask_for_setup()

    # test db connection
    conn = database_config.check_db_connection()

    # create object for database actions
    database_action = Database_actions(conn)

    # download oui.txt
    downloadFile(OUI_URL, OUI_FILE)

    # parsing oui.txt data
    with open(OUI_FILE) as infile:
        for line in infile:
            if re.search("(hex)", line):
                mac, vendor = getValuesFromLine(line)

                if mac != '' and vendor != '':
                    sql = "INSERT INTO mac_vendors "
                    sql += "(oui,vendor) "
                    sql += "VALUES ("
                    sql += strip_and_concat(mac, vendor, False)
                    sql += ")"

                    database_action.execute_query(sql)

    database_action.close_database()

    end_steps(OUI_FILE)
