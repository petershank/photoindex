from dataclasses import dataclass
from datetime import datetime


@dataclass
class Photo:
    uuid: str
    filename: str
    date: datetime
    description: str | None
    ai_caption: str | None
    detected_text: str | None