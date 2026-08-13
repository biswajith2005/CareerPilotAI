from dataclasses import dataclass
from datetime import datetime
from utils.logger import logger

from models.resume import Resume
from services.file_service import process_resume_file
from services.ai_service import ai_service


@dataclass
class ResumeAnalysis:
    ats_score: int
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]


def analyze_resume(uploaded_file):
    """
    Resume workflow.

    Sprint 3:
    Upload
        ↓
    Validation
        ↓
    Text Extraction
        ↓
    Resume Model
        ↓
    AI Analysis
    """

    logger.info(f"Resume uploaded: {uploaded_file.name}")

    result = process_resume_file(uploaded_file)

    if not result["success"]:
        logger.error(result["message"])
        raise ValueError(result["message"])
    logger.info("Resume text extracted successfully.")

    resume = Resume(
        file_name=uploaded_file.name,
        file_type=uploaded_file.type,
        raw_text=result["text"],
        uploaded_at=datetime.now(),
    )

    logger.info("Starting AI resume analysis.")

    ai_result = ai_service.analyze_resume(
        resume.raw_text
    )
    
    logger.info("AI resume analysis completed.")

    required_keys = {
        "ats_score",
        "strengths",
        "weaknesses",
        "suggestions",
    }

    if not required_keys.issubset(ai_result):
        logger.error("Invalid AI response received from Gemini.")
        raise ValueError("Invalid AI response received from Gemini.")

    analysis = ResumeAnalysis(
        ats_score=ai_result["ats_score"],
        strengths=ai_result["strengths"],
        weaknesses=ai_result["weaknesses"],
        suggestions=ai_result["suggestions"],
    )
    
    logger.info("Resume analysis completed successfully.")

    return analysis