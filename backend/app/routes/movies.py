from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Movie

router = APIRouter()

@router.get("/movies/")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()
