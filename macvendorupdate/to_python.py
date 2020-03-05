from typing import IO
import re

from misc_functions import(
    download_file,
    open_python_file,
    close_python_file,
    get_values_from_line,
    strip_and_concat,
    end_steps
)

from global_values import OUI_FILE, OUI_URL, OUTPUT_FILE_NAME


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
                mac, vendor = get_values_from_line(line)

                # n = '\t"%s": ' % mac.strip().replace("-", ":").lower()
                # n += '"%s",\n' % vendor.strip().replace("'", "`")

                n = strip_and_concat(mac, vendor)

                file.write(n)


def updatePython():
    """
        Downloads the file to process and generates a Python file (oui.py)
        with a JSON object with the MAC address and vendors.
    """

    download_file(OUI_URL, OUI_FILE)

    f = open_python_file(OUTPUT_FILE_NAME)

    writeToFile(OUI_FILE, f)

    close_python_file(f)

    end_steps(OUI_FILE)
