import requests
import os
from twilio.rest import Client

account_sid = "AC2a6347213c19905cd54c5c3ba9125cd1"
auth_token = os.environ.get("AUTH_TOKEN")
OWM = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
parameters = {
    "lat":30.9090157,
    "lon":75.851601,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(url = OWM, params =  parameters)
response.raise_for_status()
data = response.json()


will_rain = False
for hour_data in data["list"]:
    condition = hour_data["weather"][0]["id"]
    if condition < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella.☔",
        from_="whatsapp:+14155238886",
        to="Your verified phone number.",
    )
    print(message.status)


    