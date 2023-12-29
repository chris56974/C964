import csv
from pathlib import Path

base_dir = Path(__file__).parent.parent
data_dir = base_dir / "data"

ratings_csv_path = data_dir / "ratings_small.csv"
links_csv_path = data_dir / "links_small.csv"


def build_movie_id_to_imdb_id_map():
    movie_id_to_imdb_id = {}

    with open(links_csv_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            movie_id_to_imdb_id[row["movie_id"]] = row["imdb_id"]

    return movie_id_to_imdb_id


def get_user_rated_movie_ids(user_id):
    user_rated_movie_ids = []

    with open(ratings_csv_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row["user_id"] == str(user_id):
                user_rated_movie_ids.append(row["movie_id"])

    return user_rated_movie_ids


def convert_movie_ids_to_imdb_ids(movie_ids):
    movie_id_to_imdb_id = {}
    with open(links_csv_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie_id_to_imdb_id[row["movie_id"]] = row["imdb_id"]

    imdb_ids = [
        movie_id_to_imdb_id.get(movie_id)
        for movie_id in movie_ids
        if movie_id in movie_id_to_imdb_id
    ]

    return imdb_ids

def get_user_rated_imdb_ids(user_id):
    movie_ids = get_user_rated_movie_ids(user_id)
    return convert_movie_ids_to_imdb_ids(movie_ids)