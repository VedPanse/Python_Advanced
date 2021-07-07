import requests

api_key = "a31fbc7426eec7a6609cea4c99b32fc1"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 19.874811
MY_LONG = 75.317015
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
