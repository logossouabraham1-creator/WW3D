from enum import Enum

from pydantic import BaseModel, Field, StrictStr


class SubjectCategory(str, Enum):
    SPACE = "Space & Astronomy"
    NATURE = "Nature & Life"
    HUMAN_BODY = "Human Body"
    SCIENCE = "Science & Technology"
    GEOGRAPHY = "Geography"
    HISTORY = "History & Civilizations"


class Subject(BaseModel):
    name: StrictStr = Field(min_length=2, max_length=100)
    category: SubjectCategory
    description: StrictStr = Field(min_length=10)