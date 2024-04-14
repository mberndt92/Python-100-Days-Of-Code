
import requests
from datetime import datetime

URL = "https://api.sunrise-sunset.org/json"


LAT = 51.446490
LNG = 9.662290

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

now = datetime.now()

response = requests.get(URL, params=parameters)
response.raise_for_status()
print(response.json())
sunrise_hour = response.json()['results']['sunrise'].split("T")[1].split(":")[0]
sunrise_minute = response.json()['results']['sunrise'].split("T")[1].split(":")[1]

sunset_hour = response.json()['results']['sunset'].split("T")[1].split(":")[0]
sunset_minute = response.json()['results']['sunset'].split("T")[1].split(":")[1]

sunrise = ':'.join([sunrise_hour, sunrise_minute])
sunset = ':'.join([sunset_hour, sunset_minute])

print(f"Sunrise: {sunrise} | Sunset: {sunset}")
print(sunrise)