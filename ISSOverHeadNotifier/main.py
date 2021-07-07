import time

import requests
from datetime import datetime
import smtplib

MY_LAT = -19.874863
MY_LONG = 75

MY_EMAIL = "pythonved@gmail.com"
MY_PASS = "Hotpursuittritre"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


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

time_now = datetime.now()

lat_difference = 0
long_difference = 0
print(f"The lat is {iss_latitude}")
print(f"The long is {iss_longitude}")

if iss_longitude > MY_LONG:
    long_difference = round(iss_longitude - MY_LONG)
elif MY_LONG > iss_longitude:
    long_difference = round(MY_LONG - iss_longitude)

if iss_latitude > MY_LAT:
    lat_difference = round(iss_latitude - MY_LAT)
elif MY_LAT > iss_latitude:
    lat_difference = round(MY_LAT - iss_latitude)

conditions = []

if long_difference in range(6):
    conditions.append(True)
else:
    conditions.append(False)

if lat_difference in range(6):
    conditions.append(True)
else:
    conditions.append(False)


def is_dark():
    now = datetime.now()
    now = now.hour

    if now > sunset:
        return True
    elif sunset > now:
        return False


is_dark = is_dark()

while True:
    time.sleep(60)
    if False in conditions:
        print("It is far.")
    else:
        if is_dark:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs="pythonved@yahoo.com", msg="Subject: ISS\n\nLook up.")
                connection.close()
                break
        else:
            print("The ISS is above, but it is not dark yet.")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
