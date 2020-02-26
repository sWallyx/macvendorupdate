from typing import IO
import urllib.request as urllib
import re
import os

from misc_functions import dlProgress, downloadFile

from global_values import OUI_FILE, OUI_URL

def writeToFile(file_name: str, file: IO):
    """
        Opens file given by name, and writes the hex line on the final file.

        Args:
            file_name {str}: name of the file
            file {IO}: file object to write on
    """
    # parsing oui.txt data
    with open(file_name) as infile:
        for line in infile:
            if re.search("(hex)", line):
                try:
                    mac, vendor = line.strip().split("(hex)")
                except:
                    mac = vendor = ''

                n = '\t"%s": ' % mac.strip().replace("-", ":").lower()
                n += '"%s",\n' % vendor.strip().replace("'", "`")
                file.write(n)

def updatePython():
    """
        Downloads the file to process and generates a Python file (oui.py)
        with a JSON object with the MAC address and vendors.
    """
    downloadFile(OUI_URL, OUI_FILE)

    # open file and rewrite
    f = open('oui.py', 'w')
    f.write('# -*- coding: utf-8 -*-\noui = {\n')

    writeToFile(OUI_FILE, f)

    f.write('}')

    # close file
    f.close()
    print("\noui.py updated")

    print("Removing temportal file")
    # Remove downloaded file
    os.remove(OUI_FILE)

    print("Done")
