#!/usr/bin/env python
#
import re
import urllib.request as urllib
import sys
import os
import pathlib

global REM_FILE
REM_FILE = "oui.txt"


def dlProgress(count, blockSize, totalSize):
    """
        Creates a progress bar to indicate the download progress
    """
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r" + REM_FILE + " ========= -> %d%%" % percent)
    sys.stdout.flush()


def updatePython():
    OUI_URL = "http://standards.ieee.org/develop/regauth/oui/"+REM_FILE
    OUI_FILE = "oui.txt"
    # download oui.txt
    print("Downloading from", OUI_URL)
    urllib.urlretrieve(OUI_URL, OUI_FILE, reporthook=dlProgress)

    # open file and rewrite
    f = open('oui.py', 'w')
    f.write('# -*- coding: utf-8 -*-\noui = {\n')

    # parsing oui.txt data
    with open(OUI_FILE) as infile:
        for line in infile:
            if re.search("(hex)", line):
                try:
                    mac, vendor = line.strip().split("(hex)")
                except:
                    mac = vendor = ''

                n = '\t"%s": ' % mac.strip().replace("-", ":").lower()
                n += '"%s",\n' % vendor.strip().replace("'", "`")
                f.write(n)

    f.write('}')

    # close file
    f.close()
    print("\noui.py updated")

    print("Removing temportal file")
    # Remove downloaded file
    os.remove(OUI_FILE)

    print("Done")
