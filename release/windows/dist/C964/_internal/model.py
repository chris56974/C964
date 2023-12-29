from surprise import Dataset, Reader, SVD
from pathlib import Path

import pickle, os
import logging

src_dir = Path(__file__).parent

model_path = src_dir / "model.pkl"

base_dir = src_dir.parent

# Path to the data directory
data_dir = base_dir / "data"

# Path to the ratings file
ratings_csv = data_dir / "ratings_small.csv"

# Basic configuration for logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_model():
    if not os.path.exists(model_path):
        train_and_save_model()

    with open(model_path, "rb") as f:
        return pickle.load(f)


def train_and_save_model():
    try:
        logging.info("Model training started.")
        reader = Reader(
            line_format="user item rating timestamp",
            sep=",",
            rating_scale=(1, 5),
            skip_lines=1,
        )
        ratings_data = Dataset.load_from_file(file_path=ratings_csv, reader=reader)

        trainset = ratings_data.build_full_trainset()
        algo = SVD()
        algo.fit(trainset)

        with open(model_path, "wb") as f:
            pickle.dump(algo, f)

        logging.info("Model successfully trained and saved.")

    except Exception as e:
        logging.error("Error during model training: %s", e)
        raise
