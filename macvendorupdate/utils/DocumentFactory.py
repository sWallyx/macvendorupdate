""" Method to create a dummy file for testing purposes """
import os


class DocumentFactory:
    """ This class will create a file with a given name """

    def __init__(self, filename="DummyFile.txt"):
        """ Creates a DummyFile, with the given name or a made one """
        chunk = "Random text to add to the file"

        file_ = open(filename, "w")
        file_.write(chunk)
        file_.close()

        self.name = filename
        self.extension = os.path.splitext(filename)
        self.path = os.path.realpath(file_.name)
        self.file = file_

    def get_file(self):
        """ Returns the file element of the DocumentFactory """
        return self.file
