import re
import sys
import mysql.connector
import os

from modules.database import Database
from misc_functions import downloadFile

from global_values import OUI_FILE, OUI_URL

"""
	SQL minimal table needed by script:
	-- Table: mac_vendors
	-- DROP TABLE mac_vendors;
	CREATE TABLE mac_vendors
	(
	oui character varying(8) NOT NULL,
	vendor character varying NOT NULL,
	id serial NOT NULL,
	CONSTRAINT pk_mac_vendors PRIMARY KEY (oui)
	)
	WITH (
	OIDS=FALSE
	);
	ALTER TABLE mac_vendors
	OWNER TO DBUSER;
"""


def updateMysql():
    # create database_config object
    database_config = Database()

    # ask for database config
    database_config.ask_for_setup()

    # test db connection
    try:
        conn = mysql.connector.connect(
            host=database_config.db_host,
            database=database_config.db_name,
            user=database_config.db_user,
            password=database_config.db_pass
        )
    except:
        sys.exit("I am unable to connect to the database, does it really exist.")

    # download oui.txt
    downloadFile(OUI_URL, OUI_FILE)

    cur = conn.cursor()
    # parsing oui.txt data
    with open(OUI_FILE) as infile:
        for line in infile:
            if re.search("(hex)", line):
                try:
                    mac, vendor = line.strip().split("(hex)")
                except:
                    mac = vendor = ''

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
