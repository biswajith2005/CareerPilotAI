from dataclasses import dataclass


@dataclass
class ProjectAnalysis:

    project_score: int
    complexity: str
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]


def analyze_project(repo_url=None) -> ProjectAnalysis:
    """
    Dummy implementation.
    AI integration will replace this in Sprint 3.
    """

    return ProjectAnalysis(
        project_score=84,
        complexity="Intermediate",
        strengths=[
            "Good project structure",
            "Clean code organization",
            "Meaningful README",
        ],
        weaknesses=[
            "Low test coverage",
            "No deployment link",
        ],
        recommendations=[
            "Deploy the project",
            "Add unit tests",
            "Improve documentation",
        ],
    )