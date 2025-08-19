import requests
import os
from dotenv import load_dotenv

load_dotenv()

API = os.getenv("GOOGLE_SHEETS_API")
AUTH = os.getenv("AUTHORIZATION")

class DataManager:
    def __init__(self):
        self.parameters ={}
        self.data = {}
        self.api = API
        self.headers = {
            "Authorization": f"{AUTH}"
        }

    def get_cities(self):
        response = requests.get(url = self.api , headers= self.headers)
        data = response.json()
        if "prices" in data:
            self.data = data["prices"]
            return self.data
        else:
            print("DEBUG ERROR:", data)
            return []

    def update_data(self):
        for city in self.data:
            parameters = {
                "price":
                    {
                    "iataCode": city['iataCode']
                    }
            }
            response = requests.put(url= f"{API}/{city['id']}", json= parameters)
            print(response.text)

