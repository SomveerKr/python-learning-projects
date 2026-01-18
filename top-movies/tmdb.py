import requests
import os
from dotenv import load_dotenv


class TMDBClient:
    """
    A client to interact with The Movie Database (TMDB) API.
    """
    def __init__(self):
        load_dotenv()
        self.api_token = os.getenv('TMDB_ACCESS_TOKEN')
        if not self.api_token:
            raise ValueError("TMDB_ACCESS_TOKEN not found in environment variables.")

        self.base_url = "https://api.themoviedb.org/3"
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_token}"
        }

    def search_movie(self, movie_name, page=1):
        endpoint = f"{self.base_url}/search/movie"

        # Using a params dictionary handles URL encoding automatically
        params = {
            "query": movie_name,
            "include_adult": "false",
            "language": "en-US",
            "page": page
        }

        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def get_movie_detail(self, movie_id):
        endpoint = f"{self.base_url}/movie/{movie_id}?language=en-US"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None