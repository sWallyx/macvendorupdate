from macvendorupdate.misc_functions import getValuesFromLine

@pytest.mark.parametrize(("complete_string","expected_mac","expected_vendor"),("string", "mac", "vendor"))
def test_getValuesFromLine():
    text_string = ""
    mac, vendor = getValuesFromLine()

    assert mac = expected_mac
    assert vendor = expected_vendor