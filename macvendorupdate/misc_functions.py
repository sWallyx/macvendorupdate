from typing import IO
import urllib.request as urllib
import sys
import os

def dlProgress(count, blockSize, totalSize):
    """
        Creates a progress bar to indicate the download progress
    """
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r%d%%" % percent)
    sys.stdout.flush()


def downloadFile(url: str, file_name: str):
    """
        Downloads the given file from the given URL

        Args:
            url {str}: Url to search the file
            file_name {str}: Name of the file to download
    """

    print("Downloading from", url+file_name)
    urllib.urlretrieve(url+file_name, file_name, reporthook=dlProgress)


def openPythonFile(file_name: str):
    """
        Creates or opens the file if exists. And starts writing on it.

        If the file was already on the system, it will rewrite it.

        Args:
            file_name {str}: name of the file, no extension

        Return:
            python_file {IO}: file object
    """
    python_file = open(file_name + '.py', 'w')
    python_file.write('# -*- coding: utf-8 -*-\noui = {\n')

    return python_file


def closePythonFile(python_file: IO):
    """
        Closes the file, closing first the object inside it.

        Args:
            python_file {IO}:
    """
    python_file.write('}')

    # close file
    python_file.close()

    # write update to console
    print("\noui.py updated")


def getValuesFromLine(line_to_split: bytes):
    """
        Splits the line into 2 values if possible.

        Otherwise, it creates an empty line.

        Args:
            line_to_split {bytes}: line to split

        Return:
            v1 {str}: mac value, first element of split
            v2 {str}: vendor value, second element of split
    """

    try:
        v1, v2 = line_to_split.strip().split("(hex)")
    except Exception:
        v1 = v2 = ''

    return v1, v2

def strip_and_concat(mac, vendor, python_option=True):
    """
        Creates single string depending on the selected mode.

        TODO: Make it simpler without the python_option flag

        Args:
            mac {str}: mac address
            vendor {str}: vendor string
            python_option {bool}: default True. Flag to choose if
                python mode selected or mysql

        Returns:
            str: concat string with the selected format
    """
    if(python_option):
        string = '\t"%s": ' % mac.strip().replace("-", ":").lower()
        string += '"%s",\n' % vendor.strip().replace("'", "`")
    else:
        string = "'%s'," % mac.strip().replace("-", ":").lower()
        string += "'%s'" % vendor.strip().replace("'", "`")

    return string


def end_steps(file_to_remove):
    # Remove temporal file
    print("\nRemoving temportal file")
    os.remove(file_to_remove)

    print("Done!")
    print("Thanks, see you soon!")