import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, movie_data_path="movies.csv"):
        self.movies = pd.read_csv(movie_data_path)
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.movie_matrix = self.vectorizer.fit_transform(self.movies["description"])

    def recommend(self, movie_title):
        idx = self.movies[self.movies["title"] == movie_title].index[0]
        sim_scores = cosine_similarity(self.movie_matrix[idx], self.movie_matrix).flatten()
        top_indices = sim_scores.argsort()[-5:][::-1]
        return self.movies.iloc[top_indices][["title", "genre"]].to_dict(orient="records")
