import requests
from datetime import datetime

GOOGLE_SHEETS_ENDPOINT = ""  #Your Sheety endpoint
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_KEY = ""  #Your own API key generated with Nutritionix API
ID = ""  #Your own ID generated with Nutritionix API

WEIGHT = 0  #Your weight
HEIGHT = 0 #Your height
AGE = 0 #Your age

QUERY = input("Tell me which exercises you did: ")
PARAMETERS = {
    "query": QUERY,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

HEADERS = {
    "x-app-id": ID,
    "x-app-key": API_KEY,
}

RESPONSE = requests.post(url = EXERCISE_ENDPOINT, json= PARAMETERS, headers= HEADERS)
RESULTS = RESPONSE.json()

TODAY = datetime.now().strftime("%Y%m%d")
CURRENT_TIME = datetime.now().strftime("%X")

for exercise in RESULTS["exercises"]:
    SHEETS_PARAMETERS = {
        "workout":
            {
            "date": TODAY,
            "time": CURRENT_TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
            }
    }
    SHEETS_HEADERS = {
        "Authorization": "", #Your own Sheety authorization

    }
    SHEETS_RESPONSE = requests.post(url = GOOGLE_SHEETS_ENDPOINT , json =  SHEETS_PARAMETERS, headers= SHEETS_HEADERS)
    print(SHEETS_RESPONSE.text)