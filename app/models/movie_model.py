from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    director = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    genre = Column(String(50), nullable=False)
    rating = Column(Float, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
