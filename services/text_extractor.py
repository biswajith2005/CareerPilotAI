import pymupdf
from docx import Document
from pathlib import Path


def extract_pdf_text(uploaded_file) -> str:
    """Extract text from a PDF file."""

    uploaded_file.seek(0)

    pdf = pymupdf.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    uploaded_file.seek(0)

    return text


def extract_docx_text(uploaded_file) -> str:
    """Extract text from a DOCX file."""

    uploaded_file.seek(0)

    document = Document(uploaded_file)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )

    uploaded_file.seek(0)

    return text


def extract_text(uploaded_file) -> str:
    """Automatically extract text based on file type."""

    extension = Path(uploaded_file.name).suffix.lower()

    if extension == ".pdf":
        return extract_pdf_text(uploaded_file)

    if extension == ".docx":
        return extract_docx_text(uploaded_file)

    raise ValueError("Unsupported file type.")