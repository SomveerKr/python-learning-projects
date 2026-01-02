import os
import requests
from datetime import datetime
from dotenv import load_dotenv
# This line loads the environment variables from the .env file
load_dotenv()
# API Endpoints
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
LOCATIONS_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY"),
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self.get_amadeus_token()

    def get_amadeus_token(self):
        """Gets a fresh Amadeus API access token."""
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret":self._api_secret
        }
        try:
            res = requests.post(TOKEN_ENDPOINT, headers=headers, data=body)
            res.raise_for_status()
            print("Token acquired successfully!")
            return res.json()['access_token']
        except requests.exceptions.RequestException as e:
            print(f"Error getting token: {e}")
            return None

    def get_city_iata_code(self, city_name):
        """Searches for a city's IATA code using a valid token."""
        print(f"Searching for IATA code for '{city_name}'...")
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {"keyword": city_name}
        
        try:
            res = requests.get(LOCATIONS_ENDPOINT, headers=headers, params=params)
            res.raise_for_status() # This is where the 401 error was raised
            code = res.json()["data"][0]["iataCode"]
            print(code)
            return code
        except requests.exceptions.RequestException as e:
            print(f"Error searching for city: {e}")
            return None
        except (IndexError, KeyError):
            print(f"Could not find an IATA code for {city_name} in the response.")
            return None
    
    
    def search_flights_offers(self, origin_city_code, destination_city_code, from_date, to_date):
        req_header = {"Authorization": f"Bearer {self._token}"}
        req_params = {
            "originLocationCode":origin_city_code,
            "destinationLocationCode":destination_city_code,
            "departureDate": from_date,
            "returnDate": to_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": "10",
        }
        res = requests.get(FLIGHT_OFFERS_ENDPOINT, headers=req_header, params=req_params )
        if res.status_code != 200:
            print(f"check_flights() response code: {res.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", res.text)
            return None
        return res.json()