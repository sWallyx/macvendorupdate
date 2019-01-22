#!/usr/bin/env python
#
import re
import urllib
import sys
import os
import pathlib

global rem_file
rem_file = "oui.txt"

OUI_URL = "http://standards.ieee.org/develop/regauth/oui/oui.txt"
OUI_FILE = "oui.txt"

def dlProgress(count, blockSize, totalSize):
	percent = int(count*blockSize*100/totalSize)
	sys.stdout.write("\r" + rem_file + " ========= -> %d%%" % percent)
	sys.stdout.flush()

if __name__ == "__main__":
    
    # download oui.txt
	print "Downloading from",OUI_URL
	urllib.urlretrieve(OUI_URL, OUI_FILE, reporthook=dlProgress)

	# open file and rewrite
	f = open('oui.py','w')
	f.write('# -*- coding: utf-8 -*-\noui = {\n')

    # parsing oui.txt data
	with open(OUI_FILE) as infile:
		for line in infile:
		    if re.search("(hex)", line):
				try:
					mac, vendor = line.strip().split("(hex)")
				except:
					mac = vendor = ''

				n = '\t"%s": ' % mac.strip().replace("-",":").lower()
				n += '"%s",\n' % vendor.strip().replace("'","`")
				f.write(n)

	f.write('}')

	# close file
	f.close()
	print "\noui.py updated"
#
# EOF
#