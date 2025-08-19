import requests
import os
from dotenv import load_dotenv

load_dotenv()
API = "https://test.api.amadeus.com/v1"
API_KEY = os.getenv("FLIGHT_API_KEY")
API_SECRET = os.getenv("FLIGHT_API_SECRET")

class FlightSearch:
    def __init__(self):
        self.header = {}
        self.Header = {}
        self.body = {}
        self.parameters = {}
        self.token = self.get_token()

    def get_token(self):
        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.body = {
            'grant_type': 'client_credentials',
            'client_id': API_KEY,
            'client_secret': API_SECRET
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",
                                 headers=self.header, data= self.body)
        response.raise_for_status()
        token_data = response.json()
        return token_data["access_token"]

    def city_code(self, keyword):

        self.Header = {
            "Authorization": f"Bearer {self.token}"
        }
        self.parameters = {
            "keyword": keyword,
            "subType": "CITY"
        }

        response = requests.get(url = "https://test.api.amadeus.com/v1/reference-data/locations",
                                params= self.parameters, headers= self.Header)
        response.raise_for_status()
        data = response.json()
        try:
            return data["data"][0]["iataCode"]
        except (KeyError, IndexError):
            return "N/A"
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "INR",
            "max": "10",
        }

        response = requests.get(
            url=API,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()