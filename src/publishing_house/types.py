from typing import List
from pydantic import BaseModel

class ChapterOutline(BaseModel):
    title: str
    summary: str

class BookOutline(BaseModel):
    chapters: List[ChapterOutline]

class ChapterContent(BaseModel):
    title: str
    content: str