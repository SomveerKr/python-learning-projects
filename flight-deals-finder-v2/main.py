#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import time
from datetime import date, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


FROM_CITY_IATA = "DEL"

data_manager = DataManager()
flight_search = FlightSearch()
destination_cities = data_manager.destination_data
notification_manager = NotificationManager()


 # 1. Calculate the date range for the next 6 months
tomorrow = date.today() + timedelta(days=1)
six_months_from_now = tomorrow + timedelta(days=180)

# Format dates as YYYY-MM-DD strings
start_date = tomorrow.strftime("%Y-%m-%d")
end_date = six_months_from_now.strftime("%Y-%m-%d")

# ==================== Update the Airport Codes in Google Sheet ====================

for city in destination_cities:
    if  city["iataCode"] == "":
        iata_code = flight_search.get_city_iata_code(city["city"])
        city["iataCode"] = iata_code
        data_manager.update_sheet_with_iata_code(city["id"], iata_code)
        time.sleep(2)

# ==================== Search for Flights ==================== 
# ==================== Search for direct flights  ====================
for city in destination_cities: 
    print(f"Getting flights for {city['city']}...")      
    flights_data = flight_search.search_flights_offers(
        FROM_CITY_IATA, 
        city["iataCode"], 
        from_date=start_date, 
        to_date=end_date)
    cheapest_flight = find_cheapest_flight(flights_data)
    print(f"{city['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {city['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.search_flights_offers(
            FROM_CITY_IATA,
            city["iataCode"],
            from_date=start_date, 
            to_date=end_date,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")


    if cheapest_flight.price != "N/A" and cheapest_flight.price < city["lowestPrice"]:
        print(f"Lower price flight found to {city['city']}!")

        message_body = f"Low Price Alert!\nOnly {cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, on {cheapest_flight.out_date} until {cheapest_flight.return_date}"



        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only USD {cheapest_flight.price} to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only USD {cheapest_flight.price} to fly "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        print(f"Check your email. Lower price flight found to {city['city']}!")
        # notification_manager.send_sms(message_body)
