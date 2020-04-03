""" This will hold old the test for the document factory """
import pytest

from macvendorupdate.utils.DocumentFactory import DocumentFactory


@pytest.mark.parametrize(("filename"), [("randomfile.txt")])
def test_document_factory(filename):
    document = DocumentFactory(filename)
    created_document_name = document.name

    assert document.remove_file(), "The file was not found or could not be removed"
    assert (
        filename == created_document_name
    ), "File has no excepted name or was not created"
