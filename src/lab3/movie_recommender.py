import csv
from collections import defaultdict
from typing import List, Set, Dict, Tuple, Optional

class MovieRecommender:
    def __init__(self, movies_file: str, history_file: str):
        self.movies = {}
        self.history = []
        self._load_movies(movies_file)
        self._load_history(history_file)

    def _load_movies(self, filename: str) -> None:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',', 1)
                if len(parts) == 2:
                    movie_id = int(parts[0])
                    title = parts[1].strip()
                    self.movies[movie_id] = title

    def _load_history(self, filename: str) -> None:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                ids = [int(x) for x in line.split(',') if x.strip()]
                self.history.append(set(ids))

    def recommend(self, watched_ids: List[int]) -> Optional[str]:
        user_set = set(watched_ids)
        if not user_set:
            return None

        candidates = []
        for hist_set in self.history:
            common = len(hist_set & user_set)
            if common * 2 >= len(user_set):
                candidates.append(hist_set)

        candidate_movies = set()
        for hist_set in candidates:
            candidate_movies.update(hist_set - user_set)

        if not candidate_movies:
            return None

        popularity = defaultdict(int)
        for hist_set in self.history:
            for movie_id in hist_set:
                popularity[movie_id] += 1

        best_id = max(candidate_movies, key=lambda mid: popularity[mid])
        return self.movies.get(best_id)

def main():
    MOVIES_FILE = "movies.txt"
    HISTORY_FILE = "history.txt"
    recommender = MovieRecommender(MOVIES_FILE, HISTORY_FILE)
    user_input = input("Введите ID фильмов через запятую: ")
    watched = [int(x.strip()) for x in user_input.split(',') if x.strip()]
    rec = recommender.recommend(watched)
    if rec:
        print(rec)
    else:
        print("Нет рекомендаций")

if __name__ == "__main__":
    main()