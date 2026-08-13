from dataclasses import dataclass


@dataclass
class InterviewSession:

    question: str
    score: int
    feedback: list[str]


def evaluate_interview(answer=None) -> InterviewSession:
    """
    Dummy implementation.
    """

    return InterviewSession(
        question="Explain the difference between ArrayList and LinkedList.",
        score=85,
        feedback=[
            "Good explanation of internal structure.",
            "Mention time complexities.",
            "Add real-world use cases.",
        ],
    )