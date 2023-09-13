import requests
from datetime import datetime

MY_LAT = 40.712776
MY_LNG = -74.005974


def is_iss_in_range():
    # GET ISS POSITION
    # Make API Request
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    # Check for errors
    res.raise_for_status()
    # Isolate data from the response
    data = res.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True

    return False


def is_iss_visible():
    # GET MY SUNSET AND SUNRISE TIMES
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    res = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()

    data = res.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

    return False


if is_iss_in_range() and is_iss_visible():
    print("Look up")
