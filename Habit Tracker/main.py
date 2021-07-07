import requests
from datetime import datetime
# Created Username and account on pixe.la
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "pythonved"
TOKEN = "thisisaeightcharacterlongapikey"

user_params = {
    "token": "thisisaeightcharacterlongapikey",
    "username": "pythonved",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": "graph1",
    "name": "SAT Preparation",
    "unit": "Hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f" {pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()

pixel_data = {
    "date": today.strftime('%Y%m%d'),
    "quantity": "23",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
