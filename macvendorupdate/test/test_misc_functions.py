#!/env/bin/python
"""
    Test functions for pytest
"""
import pytest

from macvendorupdate.misc_functions import get_values_from_line


@pytest.mark.parametrize(
    (
        "complete_string",
        "expected_mac",
        "expected_vendor",
    ),
    (
        "08-61-95   (hex)		Rockwell Automation",
        "08-61-95",
        "Rockwell Automation",
    )
)
def test_get_values_from_line(complete_string, expected_mac, expected_vendor):

    mac, vendor = get_values_from_line(complete_string)

    assert mac == expected_mac
    assert vendor == expected_vendor
