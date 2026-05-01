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
        "genre": "Adventure",
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

@app.get('/movies')
async def getAllMovies():
    return MOVIES

@app.get("/movies/{id}")
async def getMovie(id:int):
    for movie in MOVIES:
        if movie['id'] == id:
            return movie
