from typing import IO
import urllib.request as urllib
import re
import sys
import os


REM_FILE = "oui.txt"


def dlProgress(count, blockSize, totalSize):
    """
        Creates a progress bar to indicate the download progress.
    """
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r" + REM_FILE + " ========= -> %d%%" % percent)
    sys.stdout.flush()

def downloadFileWithProgressBar(url: str, file_name: str):
    """
        Downloads the given file from the given URL

        Args:
            url {str}: Url to search the file
            file_name {str}: Name of the file to download
    """
    download_url = url+file_name

    print("Downloading from", download_url)
    urllib.urlretrieve(download_url, file_name, reporthook=dlProgress)

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
    downloadFileWithProgressBar("http://standards.ieee.org/develop/regauth/oui/", REM_FILE)

    # open file and rewrite
    f = open('oui.py', 'w')
    f.write('# -*- coding: utf-8 -*-\noui = {\n')

    writeToFile(REM_FILE, f)

    f.write('}')

    # close file
    f.close()
    print("\noui.py updated")

    print("Removing temportal file")
    # Remove downloaded file
    os.remove(REM_FILE)

    print("Done")
