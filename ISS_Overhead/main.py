import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 30.9090157
MY_LONG = 75.851601

USER = "manya79997@gmail.com"
PASSWORD = "zjcr fkyj vbbs hixw"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if 25 <= iss_latitude <= 35 and 70 <= iss_longitude <= 80 :
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url = "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >=sunset or time_now <=sunrise:
        return True
    return False


while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(from_addr=USER,
                                to_addrs="manya79997@yahoo.com",
                                msg="Subject: ISS Overhead \n\n"
                                    "LOOK UP!!!! The ISS is overhead."
                                )




