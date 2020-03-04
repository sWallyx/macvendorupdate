import pytest
from macvendorupdate.misc_functions import getValuesFromLine

@pytest.mark.parametrize(("complete_string","expected_mac","expected_vendor"),("08-61-95   (hex)		Rockwell Automation", "08-61-95", "Rockwell Automation"))
def test_getValuesFromLine(complete_string, expected_mac, expected_vendor):

    mac, vendor = getValuesFromLine(complete_string)

    assert mac == expected_mac
    assert vendor == expected_vendor