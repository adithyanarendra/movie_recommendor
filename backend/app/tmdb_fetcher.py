import os
import requests
from sqlalchemy.orm import Session
from app.database import SessionLocal, Movie, init_db

# Load TMDB API Key
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_URL = "https://api.themoviedb.org/3/movie/popular"

# Function to fetch movies from TMDB API


def fetch_movies():
    response = requests.get(TMDB_URL, params={"api_key": TMDB_API_KEY})
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

# Function to store movies in the database


def store_movies():
    init_db()  # Ensure DB is initialized
    db: Session = SessionLocal()

    movies = fetch_movies()
    for movie in movies:
        db_movie = Movie(
            id=movie["id"],
            title=movie["title"],
            overview=movie["overview"],
            rating=movie["vote_average"],
            poster_path=movie["poster_path"]
        )
        db.merge(db_movie)  # Merge prevents duplicate inserts
    db.commit()
    db.close()
    print(f"Stored {len(movies)} movies in the database.")


# Run script
if __name__ == "__main__":
    store_movies()
