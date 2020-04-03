#!/env/bin/python
"""
    Test functions for pytest misc_function file
"""
import pytest

from macvendorupdate.misc_functions import (
    get_values_from_line,
    replace_and_concat,
    simple_end,
    end_steps,
    remove_file,
)

from macvendorupdate.utils.DocumentFactory import DocumentFactory


@pytest.mark.parametrize(
    ("complete_string", "expected_mac", "expected_vendor"),
    [("08-61-95   (hex)		Rockwell Automation", "08-61-95", "Rockwell Automation")],
)
def test_get_values_from_line(complete_string, expected_mac, expected_vendor):

    mac, vendor = get_values_from_line(complete_string)

    assert mac == expected_mac
    assert vendor == expected_vendor


@pytest.mark.parametrize(
    ("mac", "vendor", "python_option", "expected_result"),
    [
        ("08-61-95", "Rockwell Automation", False, "'08:61:95','Rockwell Automation'"),
        (
            "08-61-95",
            "Rockwell Automation",
            True,
            '\t"08:61:95": "Rockwell Automation",\n',
        ),
    ],
)
def test_replace_and_concat(mac, vendor, python_option, expected_result):
    assert expected_result == replace_and_concat(mac, vendor, python_option)


@pytest.mark.parametrize(
    ("create_file", "filename"), [(True, "DummyFile.txt"), (False, "error_file.txt")]
)
def test_remove_file(create_file, filename):
    if create_file:
        file_to_remove = DocumentFactory(filename).get_file()

        remove_file(file_to_remove.name)

        try:
            open(filename)
        except FileNotFoundError:
            assert True

    else:
        if not remove_file(filename):
            assert True
        else:
            assert False


@pytest.mark.parametrize(("filename"), [("DummyFile.txt")])
def test_end_steps(filename):
    file_to_remove = DocumentFactory(filename).get_file()

    with pytest.raises(SystemExit):
        end_steps(file_to_remove.name)


def test_simple_end():
    with pytest.raises(SystemExit):
        simple_end()
