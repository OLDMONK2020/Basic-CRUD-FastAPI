from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import Optional
from app.db.database import SessionLocal
from app.schemas.movie_schema import Movie, MovieCreate
from app.services import movie_service

router = APIRouter(prefix="/movies", tags=["Movies"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[Movie])
def get_movies(genre: Optional[str] = Query(None), db: Session = Depends(get_db)):
    return movie_service.get_movies(db, genre)


@router.get("/{id}", response_model=Movie)
def get_movie(id: int = Path(gt=0), db: Session = Depends(get_db)):
    movie = movie_service.get_movie_by_id(db, id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@router.post("/", response_model=Movie)
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return movie_service.create_movie(db, movie)


@router.put("/{id}", response_model=Movie)
def update_movie(id: int, movie: MovieCreate, db: Session = Depends(get_db)):
    updated = movie_service.update_movie(db, id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated


@router.delete("/{id}")
def delete_movie(id: int, db: Session = Depends(get_db)):
    deleted = movie_service.delete_movie(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully!", "movie": deleted.title}
