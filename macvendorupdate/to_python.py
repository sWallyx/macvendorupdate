"""
    This file contains the functions for the option python
"""
import re
from typing import IO

from macvendorupdate.global_values import OUI_FILE, OUI_URL, OUTPUT_FILE_NAME
from macvendorupdate.misc_functions import (
    close_python_file,
    end_steps,
    get_values_from_line,
    open_python_file,
    replace_and_concat,
)

from macvendorupdate.modules.download_module import Download

def write_to_file(file_name: str, file: IO):
    """
        Opens file given by name, and writes the hex line on the final file.

        Args:
            file_name {str}: name of the file
            file {IO}: file object to write on
    """

    with open(file_name) as in_file:
        for line in in_file:
            if re.search("(hex)", line):
                mac, vendor = get_values_from_line(line)

                record = replace_and_concat(mac, vendor)

                file.write(record)


def update_python():
    """
        Downloads the file to process and generates a Python file (oui.py)
        with a JSON object with the MAC address and vendors.
    """

    Download(OUI_URL + OUI_FILE, OUI_FILE)

    file_ = open_python_file(OUTPUT_FILE_NAME)

    write_to_file(OUI_FILE, file_)

    close_python_file(file_)

    end_steps(OUI_FILE)
