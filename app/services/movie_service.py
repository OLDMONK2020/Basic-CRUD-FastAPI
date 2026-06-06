from sqlalchemy.orm import Session
from app.repositories import movie_repository
from app.schemas.movie_schema import MovieCreate


def get_movies(db: Session, genre: str | None = None):
    return movie_repository.get_movies(db, genre)


def get_movie_by_id(db: Session, movie_id: int):
    return movie_repository.get_movie_by_id(db, movie_id)


def create_movie(db: Session, movie: MovieCreate):
    return movie_repository.create_movie(db, movie)


def update_movie(db: Session, movie_id: int, movie: MovieCreate):
    return movie_repository.update_movie(db, movie_id, movie)


def delete_movie(db: Session, movie_id: int):
    return movie_repository.delete_movie(db, movie_id)
