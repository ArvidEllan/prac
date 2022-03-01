import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

paraameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=paraameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":"[0]))
sunset =  int(data["results"]["sunset"].split("T")[1].split(":"[0]))

time_now = datetime.now()