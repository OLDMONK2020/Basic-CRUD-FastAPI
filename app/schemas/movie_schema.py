from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class MovieBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    director: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1900, lt=datetime.now().year)
    genre: str = Field(..., min_length=1, max_length=50)
    rating: float = Field(..., ge=0, le=10)
    duration_minutes: int = Field(..., gt=10)


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True
