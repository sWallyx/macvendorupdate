from typing import IO
import urllib.request as urllib
import sys
import os

from macvendorupdate.global_values import OUI_FILE, OUI_URL


def download_progress(count, block_size, total_size):
    """
        Creates a progress bar to indicate the download progress
    """
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r%d%%" % percent)
    sys.stdout.flush()


def download_file(url: str = OUI_URL, file_name: str = OUI_FILE):
    """
        Downloads the given file from the given URL

        Args:
            url {str}: Url to search the file
            file_name {str}: Name of the file to download
    """

    print("Downloading from", url + file_name)
    urllib.urlretrieve(url + file_name, file_name, reporthook=download_progress)


def open_python_file(file_name: str):
    """
        Creates or opens the file if exists. And starts writing on it.

        If the file was already on the system, it will rewrite it.

        Args:
            file_name {str}: name of the file, no extension

        Returns:
            IO: file object
    """
    python_file = open(file_name + ".py", "w")
    python_file.write("# -*- coding: utf-8 -*-\noui = {\n")

    return python_file


def close_python_file(python_file: IO):
    """
        Closes the file, closing first the object inside it.

        Args:
            python_file {IO}:
    """
    python_file.write("}")

    # close file
    python_file.close()

    # write update to console
    print("\noui.py updated")


def get_values_from_line(line_to_split: bytes):
    """
        Splits the line into 2 values if possible.

        Otherwise, it creates an empty line.

        Args:
            line_to_split {bytes}: line to split

        Returns:
            str: mac value, first element of split
            str: vendor value, second element of split
    """

    try:
        first_strip, second_strip = line_to_split.strip().split("(hex)")
    except ValueError:
        first_strip = second_strip = ""

    return first_strip.strip(), second_strip.strip()


def replace_and_concat(mac, vendor, python_option=True):
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
    if python_option:
        string = '\t"%s": ' % mac.replace("-", ":").lower()
        string += '"%s",\n' % vendor.replace("'", "`")
    else:
        string = "'%s'," % mac.replace("-", ":").lower()
        string += "'%s'" % vendor.replace("'", "`")

    return string


def end_steps(file_to_remove):
    """
        Step to end the application, by removing the file and
        showing a message.
    """
    # Remove temporal file
    print("\nRemoving temportal file")
    os.remove(file_to_remove)

    print("Done!")
    print("Thanks, see you soon!")
    raise SystemExit


def simple_end():
    print("Thanks, see you soon!")
    raise SystemExit
