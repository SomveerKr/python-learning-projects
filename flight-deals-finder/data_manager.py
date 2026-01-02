import requests
import os
from dotenv import load_dotenv
# This line loads the environment variables from the .env file
load_dotenv()
SHEETY_ENDPOINT = f"https://api.sheety.co/{os.getenv("GOOGLE_SHEET_ID")}/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers ={"Authorization": f"Bearer {os.getenv("SHEETY_BEARER_TOKEN")}"}
        self.destination_data = self.get_data_from_sheety()


    def get_data_from_sheety(self):
        res = requests.get(f"{SHEETY_ENDPOINT}", headers=self.headers)
        res.raise_for_status()

        data = res.json()
        print(res.status_code)
        return data["prices"]

    def update_sheet_with_iata_code(self, id, iata_code):
        url= f"{SHEETY_ENDPOINT}/{id}"
        body = {
            "price": {
               "iataCode": iata_code
            }
            }
        res = requests.put(url=url, headers=self.headers, json=body)
        print(res.status_code)
