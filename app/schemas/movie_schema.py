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


"""
🟢

👉 class MovieCreate(MovieBase): pass

This defines a schema for creating a new movie.
It inherits all fields from MovieBase (like title, director, year, etc.).
The pass means “no extra fields” — it’s just a direct reuse of MovieBase.

Why? 
When you create a new movie, you don’t provide an id (the database generates it). So MovieCreate is the input schema for POST requests.

👉 class Movie(MovieBase): id: int

This defines the schema for a movie object returned from the API.
It inherits all fields from MovieBase and adds an id field.

Why? 
When you fetch movies from the database, each one has a unique id. So this schema is used for responses (GET requests).

👉 class Config: from_attributes = True

This is a Pydantic v2 feature.
It tells Pydantic: “You can build this schema directly from ORM objects (SQLAlchemy models).”
Without this, if you tried to return a SQLAlchemy Movie object from your API, FastAPI wouldn’t know how to convert it into a Pydantic schema.

🔴
"""
