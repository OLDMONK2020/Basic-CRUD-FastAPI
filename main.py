from fastapi import FastAPI

app = FastAPI()

MOVIES = [
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

# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/movies?genre=Sci-Fi'


@app.get("/movies")
async def getMoviesByGenre(genre: str | None = None):
    if genre:
        movie_list = []
        for movie in MOVIES:
            if movie.get("genre").casefold() == genre.casefold():
                movie_list.append(movie)
        return movie_list
    else:
        return MOVIES


# http://127.0.0.1:8000/movies/2


@app.get("/movies/{id}")
async def getMoviesById(id: int | None = None):
    if id:
        for movie in MOVIES:
            if movie.get("id") == id:
                return movie
    else:
        return {"error": "Movie not found"}
