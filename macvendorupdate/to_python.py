"""
    This file contains the functions for the option python
"""
from typing import IO
import re

from misc_functions import (
    download_file,
    open_python_file,
    close_python_file,
    get_values_from_line,
    replace_and_concat,
    end_steps,
)

from global_values import OUI_FILE, OUI_URL, OUTPUT_FILE_NAME


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

    download_file(OUI_URL, OUI_FILE)

    file_ = open_python_file(OUTPUT_FILE_NAME)

    write_to_file(OUI_FILE, file_)

    close_python_file(file_)

    end_steps(OUI_FILE)
