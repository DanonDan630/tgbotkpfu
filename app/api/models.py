from pydantic import BaseModel, Field
from typing import List, Optional


class Group(BaseModel):
    number: str = Field(..., title="Group number", max_length=7)

class ScheduleFull(BaseModel):
    data: dict = Field(..., title="Full data")
    status_code: int = Field(..., title="Status code")