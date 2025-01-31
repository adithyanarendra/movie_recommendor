from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db, Movie
from .routes import movies, recommend

app = FastAPI()

router = APIRouter()

app.include_router(movies.router)
app.include_router(recommend.router)


@app.get("/")
def root():
    return {"message": "Movie Recommender API"}


@router.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()
