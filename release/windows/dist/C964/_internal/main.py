import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView

import webbrowser

from recommendations import get_recommended_movie_imdb_ids
from ratings import get_user_rated_imdb_ids

kivy.require("2.2.1")


class MovieRecommenderApp(App):
    def build(self):
        self.title = "C964 - Movie Recommender"
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # User ID Input Bar
        input_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50)
        self.user_id_input = TextInput(
            text="", multiline=False, input_filter="int", size_hint_x=0.3
        )
        input_layout.add_widget(Label(text="Enter a user id (1 - 671):"))
        input_layout.add_widget(self.user_id_input)

        # Buttons for fetching data
        fetch_rated_button = Button(text="Fetch Rated", size_hint_x=0.3)
        fetch_rated_button.bind(on_press=self.get_user_rated_movies)
        fetch_recommendations_button = Button(
            text="Fetch Recommendations", size_hint_x=0.6
        )
        fetch_recommendations_button.bind(on_press=self.get_recommendations)

        input_layout.add_widget(fetch_rated_button)
        input_layout.add_widget(fetch_recommendations_button)
        layout.add_widget(input_layout)

        # Common ScrollView for Rated and Recommended Movies
        self.movies_layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.movies_layout.bind(minimum_height=self.movies_layout.setter("height"))
        self.movies_scroll = ScrollView(size_hint=(1, 0.4), do_scroll_x=False)
        self.movies_scroll.add_widget(self.movies_layout)
        layout.add_widget(self.movies_scroll)

        # Image Display
        self.current_image = Image(size_hint_y=1)
        layout.add_widget(self.current_image)

        # Image Buttons
        button_layout = BoxLayout(orientation="horizontal", size_hint_y=0.2)
        imgs = [
            "mostRated.png",
            "userRatingsDistribution.png",
            "kmeans.png",
            "nondescriptive.png",
        ]

        for img in imgs:
            btn = Button(text=img, size_hint_y=None, width=200)
            btn.bind(on_press=lambda instance, x=img: self.show_image(x))
            button_layout.add_widget(btn)
        layout.add_widget(button_layout)

        return layout

    def update_movie_list(self, movies, list_type):
        self.movies_layout.clear_widgets()
        prefix = "Rated - " if list_type == "rated" else "Recommended - "
        for movie in movies:
            label_text = f"{prefix}Click Me! IMDB ID {movie}"
            movie_button = Button(text=label_text, size_hint_y=None, height=40, background_color=(1,0,1,1))
            movie_button.bind(on_press=lambda instance, x=movie: self.open_imdb_link(x))
            self.movies_layout.add_widget(movie_button)

    def get_user_rated_movies(self, instance):
        user_id = self.user_id_input.text
        if user_id.isdigit():
            user_id = int(user_id)
            rated_movies = get_user_rated_imdb_ids(user_id)
            self.update_movie_list(rated_movies, "rated")

    def get_recommendations(self, instance):
        user_id = self.user_id_input.text
        if user_id.isdigit():
            user_id = int(user_id)
            recommendations = get_recommended_movie_imdb_ids(user_id)
            self.update_movie_list(recommendations, "recommended")

    def open_imdb_link(self, imdb_id):
        imdb_url = f"https://www.imdb.com/title/tt{imdb_id}"
        webbrowser.open(imdb_url)

    def show_image(self, img_name):
        self.current_image.source = f"../imgs/{img_name}"


if __name__ == "__main__":
    MovieRecommenderApp().run()
