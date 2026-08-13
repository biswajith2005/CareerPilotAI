from dataclasses import dataclass
from datetime import datetime


@dataclass
class Resume:

    file_name: str
    file_type: str
    raw_text: str
    uploaded_at: datetime