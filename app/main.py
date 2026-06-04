from datetime import datetime
from fastapi import FastAPI, Query, Path, HTTPException
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()


class MovieModel(BaseModel):
    # id is optional, auto-generated
    id: Optional[int] = Field(None, gt=0)
    title: str = Field(..., min_length=1, max_length=100)
    director: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., ge=1900, lt=datetime.now().year)
    genre: str = Field(..., min_length=1, max_length=50)
    rating: float = Field(..., ge=0, le=10)
    duration_minutes: int = Field(..., gt=10)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Inception",
                "director": "Christopher Nolan",
                "year": 2010,
                "genre": "Sci-Fi",
                "rating": 8.8,
                "duration_minutes": 148,
            }
        }
    }


MOVIES: list[dict] = [
    {
        "id": 1,
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "genre": "Sci-Fi",
        "rating": 8.8,
        "duration_minutes": 148,
    },
    {
        "id": 2,
        "title": "The Dark Knight",
        "director": "Christopher Nolan",
        "year": 2008,
        "genre": "Action",
        "rating": 9.0,
        "duration_minutes": 152,
    },
    {
        "id": 3,
        "title": "Interstellar",
        "director": "Christopher Nolan",
        "year": 2014,
        "genre": "Sci-Fi",
        "rating": 8.6,
        "duration_minutes": 169,
    },
    {
        "id": 4,
        "title": "Parasite",
        "director": "Bong Joon-ho",
        "year": 2019,
        "genre": "Thriller",
        "rating": 8.6,
        "duration_minutes": 132,
    },
    {
        "id": 5,
        "title": "Avengers: Infinity War",
        "director": "Anthony & Joe Russo",
        "year": 2018,
        "genre": "Superhero",
        "rating": 8.4,
        "duration_minutes": 149,
    },
]


@app.get("/movies", response_model=list[MovieModel])
async def getMoviesByGenre(
    genre: Optional[str] = Query(default=None, min_length=1, max_length=50)
):
    if genre:
        return [
            movie for movie in MOVIES if movie["genre"].casefold() == genre.casefold()
        ]
    return MOVIES


@app.get("/movies/{id}", response_model=MovieModel)
async def getMovieById(id: int = Path(gt=0)):
    for movie in MOVIES:
        if movie["id"] == id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.post("/movies", response_model=list[MovieModel])
async def addNewMovie(movie: MovieModel):
    new_movie = setId(movie)
    MOVIES.append(new_movie)
    return MOVIES


@app.put("/movies/{id}", response_model=list[MovieModel])
async def updateMovie(id: int, movieParam: MovieModel):
    for index, movie in enumerate(MOVIES):
        if movie["id"] == id:
            MOVIES[index] = movieParam.model_dump()
            MOVIES[index]["id"] = id  # preserve id
            return MOVIES
    raise HTTPException(status_code=404, detail="Movie not found")


@app.delete("/movies/{id}")
async def deleteMovie(id: int):
    for index, movie in enumerate(MOVIES):
        if movie["id"] == id:
            deleted = MOVIES.pop(index)
            return {"message": "Movie deleted successfully!", "movie": deleted["title"]}
    raise HTTPException(status_code=404, detail="Movie not found")


def setId(movie: MovieModel) -> dict:
    new_movie = movie.model_dump()
    new_movie["id"] = len(MOVIES) + 1
    return new_movie


# 🔑 Rule of Thumb
# If you’re storing Pydantic models → use movie.title.
# Why: Pydantic models expose fields as attributes, so you can use dot notation like in JavaScript objects.

# If you’re storing dicts → use movie["title"] or movie.get("title") (safer)
# Why: Dicts in Python are like plain JS objects — you access values by key
