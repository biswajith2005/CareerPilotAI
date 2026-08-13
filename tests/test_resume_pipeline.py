from io import BytesIO

from utils.validators import validate_resume_file
from utils.text_cleaner import clean_resume_text


class DummyFile(BytesIO):
    def __init__(self, content: bytes, name: str):
        super().__init__(content)
        self.name = name


def test_valid_pdf():
    file = DummyFile(b"dummy", "resume.pdf")
    valid, _ = validate_resume_file(file)
    assert valid


def test_invalid_extension():
    file = DummyFile(b"dummy", "resume.exe")
    valid, _ = validate_resume_file(file)
    assert not valid


def test_empty_file():
    file = DummyFile(b"", "resume.pdf")
    valid, _ = validate_resume_file(file)
    assert not valid


def test_text_cleaner():

    dirty = "Hello\n\n\n\nWorld      Python"

    cleaned = clean_resume_text(dirty)

    assert "World Python" in cleaned