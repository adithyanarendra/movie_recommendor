from fastapi import APIRouter, HTTPException
from ..ml.recommender import MovieRecommender

router = APIRouter()
recommender = MovieRecommender()

@router.get("/recommend/")
def get_recommendations(movie_title: str):
    try:
        return recommender.recommend(movie_title)
    except:
        raise HTTPException(status_code=404, detail="Movie not found")
