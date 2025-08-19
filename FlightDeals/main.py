import time
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_data import find_cheapest_flight
from datetime import datetime,timedelta
from flight_search import FlightSearch

DATA_MANAGER= DataManager()
sheet_data = DATA_MANAGER.get_cities()

FLIGHT_SEARCH = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY = "DEL"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = FLIGHT_SEARCH.city_code(row["city"])
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

DATA_MANAGER.data = sheet_data
DATA_MANAGER.update_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = FLIGHT_SEARCH.check_flights(
        ORIGIN_CITY,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
