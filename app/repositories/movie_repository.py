from sqlalchemy.orm import Session
from app.models.movie_model import Movie
from app.schemas.movie_schema import MovieCreate


def get_movies(db: Session, genre: str | None = None):
    query = db.query(Movie)
    if genre:
        query = query.filter(Movie.genre.ilike(genre))
    return query.all()


def get_movie_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def update_movie(db: Session, movie_id: int, movie: MovieCreate):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_movie:
        for key, value in movie.dict().items():
            setattr(db_movie, key, value)
        db.commit()
        db.refresh(db_movie)
    return db_movie


def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_movie:
        db.delete(db_movie)
        db.commit()
    return db_movie
