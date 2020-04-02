import requests
from progress.bar import Bar
from progress.spinner import Spinner

class Download:
    def __init__(self, origin_url: str, save_file: str):
        """
            This download module, receives 2 parameters, the URL to get the file from
            and a name to store that file. It will start the download process and will
            show a progress or spinner depending if it can obtain the size of the file.

            Arguments:
                origin_url {str}: URL where the file is located
                save_file {str}: Where the content of the file is gonna be saved
        """
        request_call = requests.get(origin_url, stream=True)

        file_size = request_call.headers['content-length']
        if file_size:
            progress_status = Bar(save_file, max=int(file_size))
        else:
            progress_status = Spinner(save_file)

        with open(save_file, 'wb') as file_:
            for chunk in request_call.iter_content(chunk_size=1024*50):
                if chunk: # filter out keep-alive new chunks
                    progress_status.next(len(chunk))
                    file_.write(chunk)

        progress_status.finish()