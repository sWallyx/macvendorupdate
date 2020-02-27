import re
import mysql.connector
import os

from modules.database_settings import Database_settings
from misc_functions import downloadFile, getValuesFromLine

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

    # get cursor
    cur = conn.cursor()

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
                    sql += "'%s'," % mac.strip().replace("-", ":").lower()
                    sql += "'%s'" % vendor.strip().replace("'", "`")
                    sql += ")"
                    print(sql)
                    try:
                        cur.execute(sql)
                        conn.commit()
                    except mysql.connector.Error as err:
                        print("Something went wrong: {}".format(err))

    cur.close()
    conn.close()

    # Remove temporal file
    print("\nRemoving temportal file")
    # Remove downloaded file
    os.remove(OUI_FILE)

    print("Done")
