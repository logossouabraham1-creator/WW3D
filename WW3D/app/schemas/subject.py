from enum import Enum
# The Enum is to define a fixed set of named values e.g Days of the week or Traffic lights.
from pydantic import BaseModel, Field, StrictStr
# pydantic is where you describe the shape of your data as a class,and it automatically checks and converts incoming data to match.

# This class inherits from  both Enum and str e.g multiple inheritance
# The arrangement is positional 
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