from dataclasses import dataclass


@dataclass
class Roadmap:

    role: str
    duration: str
    skills: list[str]
    milestones: list[str]


def generate_roadmap(role=None) -> Roadmap:
    """
    Dummy implementation.
    """

    return Roadmap(
        role="Software Engineer",
        duration="12 Weeks",
        skills=[
            "DSA",
            "Java",
            "SQL",
            "System Design",
            "Projects",
        ],
        milestones=[
            "Week 1-2 : DSA Fundamentals",
            "Week 3-5 : Backend Development",
            "Week 6-8 : Projects",
            "Week 9-12 : Interview Preparation",
        ],
    )