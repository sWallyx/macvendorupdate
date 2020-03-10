#!/env/bin/python
"""
    Test functions for pytest misc_function file
"""
import pytest

from macvendorupdate.misc_functions import get_values_from_line, strip_and_concat


@pytest.mark.parametrize(
    (
        "complete_string",
        "expected_mac",
        "expected_vendor",
    ),
    [
        (
            "08-61-95   (hex)		Rockwell Automation",
            "08-61-95",
            "Rockwell Automation",
        ),
    ]
)
def test_get_values_from_line(complete_string, expected_mac, expected_vendor):

    mac, vendor = get_values_from_line(complete_string)

    assert mac == expected_mac
    assert vendor == expected_vendor


@pytest.mark.parametrize(
    (
        "mac",
        "vendor",
        "python_option",
        "expected_result"
    ),
    [
        (
            "08-61-95",
            "Rockwell Automation",
            False,
            "'08:61:95','Rockwell Automation'",
        ),
        (
            "08-61-95",
            "Rockwell Automation",
            True,
            '\t"08:61:95": "Rockwell Automation",\n',
        ),
    ]
)
def test_strip_and_concat(mac, vendor, python_option, expected_result):
    assert expected_result == strip_and_concat(mac, vendor, python_option)
