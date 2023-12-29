from model import get_model
from ratings import convert_movie_ids_to_imdb_ids


def get_recommended_movie_ids(user_id):
    model = get_model()
    trainset = model.trainset

    # Retrieve the movies already rated by the specific user
    user_ratings = trainset.ur[trainset.to_inner_uid(str(user_id))]
    rated_movies = [iid for (iid, _) in user_ratings]

    # Predict ratings for all movies the user hasn't rated yet
    all_movies = trainset.all_items()
    unrated_movies = [
        trainset.to_raw_iid(iid) for iid in all_movies if iid not in rated_movies
    ]
    predictions = [model.predict(str(user_id), iid) for iid in unrated_movies]

    # Get top 5 recommendations
    top_recommendations = sorted(predictions, key=lambda x: x.est, reverse=True)[:5]

    # Return movie IDs of top recommendations
    return [rec.iid for rec in top_recommendations]


def get_recommended_movie_imdb_ids(user_id):
    movie_ids = get_recommended_movie_ids(user_id)
    return convert_movie_ids_to_imdb_ids(movie_ids)
