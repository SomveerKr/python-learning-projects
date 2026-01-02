import requests
import os
from dotenv import load_dotenv
# This line loads the environment variables from the .env file
load_dotenv()
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{os.getenv("GOOGLE_SHEET_ID")}/flightDeals/prices"
SHEETY_USERS_ENDPOINT = f"https://api.sheety.co/{os.getenv("GOOGLE_SHEET_ID")}/flightDeals/users"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers ={"Authorization": f"Bearer {os.getenv("SHEETY_BEARER_TOKEN")}"}
        self.destination_data = self.get_data_from_sheety()


    def get_data_from_sheety(self):
        res = requests.get(f"{SHEETY_PRICES_ENDPOINT}", headers=self.headers)
        res.raise_for_status()

        data = res.json()
        print(res.status_code)
        return data["prices"]

    def update_sheet_with_iata_code(self, id, iata_code):
        url= f"{SHEETY_PRICES_ENDPOINT}/{id}"
        body = {
            "price": {
               "iataCode": iata_code
            }
            }
        res = requests.put(url=url, headers=self.headers, json=body)
        print(res.status_code)
    def get_customer_emails(self):
        res = requests.get(f"{SHEETY_USERS_ENDPOINT}", headers=self.headers)
        res.raise_for_status()

        data = res.json()
        print(res.status_code)
        return data["users"]
