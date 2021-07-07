import requests
from datetime import datetime

GENDER = "MALE"
WEIGHT_KG = "69"
HEIGHT_CM = "183"
AGE = "16"

APP_ID = "0a813028"
API_KEY = "4372864ec1ddf0ac3b941a13682e7393"

exercise_endpoint = "https://trackapi.nutrionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/"
exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

sheet_response = requests.post(
    sheet_endpoint, json=sheet_inputs,
    auth=(
        "ved",
        "Hotpursuittritre"
    )
)

bearer_headers = {
    "Authorization": ""
}
