import requests

MY_LAT = 19.874839
MY_LONG = 75.316956

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)
print(data["results"]["sunrise"].split("T")[1].split(":")[0])
