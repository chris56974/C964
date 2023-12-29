import unittest
from ratings import convert_movie_ids_to_imdb_ids, get_user_rated_movie_ids


class TestRatings(unittest.TestCase):
    def test_convert_movie_ids_to_imdb_ids(self):
        movie_ids = ["31"]
        expected_imdb_ids = ["0112792"]
        actual_imdb_ids = convert_movie_ids_to_imdb_ids(movie_ids)
        self.assertEqual(expected_imdb_ids, actual_imdb_ids)

    def test_get_user_rated_movie_ids(self):
        user_id = 1
        expected_movie_ids = [
            "31",
            "1029",
            "1061",
            "1129",
            "1172",
            "1263",
            "1287",
            "1293",
            "1339",
            "1343",
            "1371",
            "1405",
            "1953",
            "2105",
            "2150",
            "2193",
            "2294",
            "2455",
            "2968",
            "3671",
        ]
        actual_movie_ids = get_user_rated_movie_ids(user_id)
        self.assertEqual(expected_movie_ids, actual_movie_ids)


if __name__ == "__main__":
    unittest.main()
