from utils.validators import validate_resume_file
from services.text_extractor import extract_text
from utils.text_cleaner import clean_resume_text


def process_resume_file(uploaded_file):
    """
    Validate the uploaded resume and extract its text.

    Returns:
        dict:
        {
            "success": bool,
            "message": str,
            "text": str
        }
    """

    is_valid, message = validate_resume_file(uploaded_file)

    if not is_valid:
        return {
            "success": False,
            "message": message,
            "text": ""
        }

    extracted_text = extract_text(uploaded_file)
    clean_text = clean_resume_text(extracted_text)

    return {
    "success": True,
    "message": "Resume processed successfully.",
    "text": clean_text
}