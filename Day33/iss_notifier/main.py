import requests
import smtplib
from datetime import datetime
import time


MY_LAT = 51.446490  # Your latitude
MY_LONG = 9.662290  # Your longitude


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_in_sight(lat, lng):
    if abs(MY_LAT - lat) <= 5:
        if abs(MY_LONG - lng) <= 5:
            return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    return time_now >= sunset or time_now <= sunrise


def send_mail(subject, msg, to):
    my_email = "maximilian.berndt92@gmail.com"
    password = "ndwrgnyoyjeicqie"

    formatted_msg = f"Subject: {subject}\n\n{msg}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to,
            msg=formatted_msg
        )

def get_iss_lat_lng():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude, iss_longitude


def send_email_if_iss_is_close():
    iss_latitude, iss_longitude = get_iss_lat_lng()
    iss_in_sight = is_iss_in_sight(lat=iss_latitude, lng=iss_longitude)
    print(f"Current position: ({iss_latitude}|{iss_longitude}) vs. my_pos:({MY_LAT}|{MY_LONG})")

    if iss_in_sight and is_night():
        print("You should see it right now!")
        send_mail(
            subject="ISS is close!",
            msg="Look up, the ISS is currently flying over you",
            to="maximilian_berndt@icloud.com"
        )


while True:
    send_email_if_iss_is_close()
    time.sleep(60)

