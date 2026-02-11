from typing import List
from pydantic import BaseModel, Field

class ChapterOutline(BaseModel):
    title: str
    summary: str

class BookOutline(BaseModel):
    chapters: List[ChapterOutline]

class ChapterContent(BaseModel):
    title: str
    content: str


class DocxWriterInput(BaseModel):
    file_path: str = Field(..., description="Path where the DOCX file will be saved. Example: output/book.docx")
    title: str = Field(..., description="Title of the document/book")
    content: str = Field(..., description="Full book text content formatted in chapters and sections")
