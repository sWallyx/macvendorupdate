import urllib.request as urllib
import sys

def dlProgress(count, blockSize, totalSize):
    """
        Creates a progress bar to indicate the download progress
    """
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r ...%d%%" % percent)
    sys.stdout.flush()

def downloadFile(url: str, file_name: str):
    """
        Downloads the given file from the given URL

        Args:
            url {str}: Url to search the file
            file_name {str}: Name of the file to download
    """
    download_url = url+file_name

    print("Downloading from", download_url)
    urllib.urlretrieve(download_url, file_name, reporthook=dlProgress)