#!/usr/bin/env python
#
import re
import urllib
import sys
import mysql.connector
import os

# global variable to be used in dlProgress
global rem_file
rem_file = "oui.txt"
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
#

OUI_URL = "http://standards.ieee.org/develop/regauth/oui/oui.txt"
OUI_FILE = "oui.txt"

def dlProgress(count, blockSize, totalSize):
	percent = int(count*blockSize*100/totalSize)
	sys.stdout.write("\r" + rem_file + "...%d%%" % percent)
	sys.stdout.flush()
#
#
def updateMysql():
	# get database info
	print "Insert the database info"
	setHost = raw_input("\nSet the host:  ")
	setDb = raw_input("\nSet the database:  ")
	setUser = raw_input("\nSet the user:  ")
	setPword = raw_input("\nSet the password:  ")

    #
    # download oui.txt
	print "Downloading ",OUI_URL
	urllib.urlretrieve(OUI_URL, OUI_FILE, reporthook=dlProgress)
    #
    #connect to db
	try:
		conn = mysql.connector.connect(host=setHost,database=setDb,user=setUser,password=setPword)
	except:
		sys.exit("I am unable to connect to the database")
    #
	cur = conn.cursor()
    # parsing oui.txt data
	with open(OUI_FILE) as infile:
		for line in infile:
		    if re.search("(hex)", line):
				try:
					mac,vendor = line.strip().split("(hex)")
				except:
					mac = vendor = ''

				if mac!='' and vendor!='':
					sql = "INSERT INTO mac_vendors "
					sql+= "(oui,vendor) "
					sql+= "VALUES ("
					sql+= "'%s'," % mac.strip().replace("-",":").lower()
					sql+= "'%s'" % vendor.strip().replace("'","`")
					sql+= ")"
					print sql
					try:
						cur.execute(sql)
						conn.commit()
					except mysql.connector.Error as err:
						print("Something went wrong: {}".format(err))

	cur.close()
	conn.close()

	#Remove temporal file
	print "Removing temportal file"
	# Remove downloaded file
	os.remove(OUI_FILE)

	print "Done"
	