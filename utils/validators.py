from pathlib import Path

# Supported resume formats
ALLOWED_RESUME_EXTENSIONS = {".pdf", ".docx"}

# Maximum file size (5 MB)
MAX_RESUME_SIZE = 5 * 1024 * 1024


def validate_resume_file(uploaded_file):
    """
    Validate the uploaded resume.

    Returns:
        tuple[bool, str]
        (True, "") if valid
        (False, "Reason") if invalid
    """

    if uploaded_file is None:
        return False, "Please upload a resume."

    extension = Path(uploaded_file.name).suffix.lower()

    if extension not in ALLOWED_RESUME_EXTENSIONS:
        return False, "Only PDF and DOCX files are supported."

    uploaded_file.seek(0, 2)
    file_size = uploaded_file.tell()
    uploaded_file.seek(0)

    if file_size == 0:
        return False, "The uploaded file is empty."

    if file_size > MAX_RESUME_SIZE:
        return False, "Resume size cannot exceed 5 MB."

    return True, ""