"""
    This script will call to the download class just to
    make a simple download
"""
from macvendorupdate.global_values import OUI_FILE, OUI_URL, OUTPUT_FILE_NAME
from macvendorupdate.modules.download_module import Download


def download_file():
    """ Calls the Download class to download a file """
    Download(OUI_URL + OUI_FILE, OUI_FILE)
