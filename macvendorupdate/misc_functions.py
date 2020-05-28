import os
from typing import IO


def open_python_file(file_name: str) -> IO:
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


def get_values_from_line(line_to_split: bytes) -> [str, str]:
    """
        Splits the line into 2 values if possible.

        Otherwise, it creates an empty line.

        Args:
            line_to_split {bytes}: line to split

        Returns:
            [str, str]: mac value, vendor value
    """

    try:
        first_strip, second_strip = line_to_split.strip().split("(hex)")
    except ValueError:
        first_strip = second_strip = ""

    return first_strip.strip(), second_strip.strip()


def replace_and_concat(mac: str, vendor: str, python_option=True) -> str:
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


def end_steps(file_to_remove: str):
    """
        Step to end the application, by removing the file and
        showing a message.
    """
    # Remove temporal file
    remove_file(file_to_remove)

    print("Done!")
    print("Thanks, see you soon!")
    raise SystemExit


def simple_end():
    """ Just ends the app """
    print("Thanks, see you soon!")
    raise SystemExit


def remove_file(file_to_remove: str):
    """ Removes the given file, caches FileNotFoundError exception """
    print("\nRemoving temportal file")
    try:
        os.remove(file_to_remove)
    except FileNotFoundError:
        pass
