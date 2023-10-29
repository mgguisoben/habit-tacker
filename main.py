import datetime as dt
import os

import requests

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")  # Uniques token that user defines
PIXELA_UNAME = os.environ.get("PIXELA_UNAME")   # Unique username
graph_id = "graph5"

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# Create User

PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_UNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_response = requests.post(url=PIXELA_USER_ENDPOINT, json=user_params)
print(pixela_response.text)  # Prints response as a text

# Creating graph

PIXELA_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_UNAME}/graphs"

graph_params = {
    "id": graph_id,
    "name": "Python Learning Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

pixela_response = requests.post(url=PIXELA_GRAPH_ENDPOINT, headers=headers, json=graph_params)
print(pixela_response.text)

# Adding pixels

today = dt.datetime.strftime(dt.datetime.now(), "%Y%m%d")

PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_UNAME}/graphs/{graph_id}"

pixel_params = {
    'date': today,
    'quantity': '10'
}

pixel_response = requests.post(url=PIXEL_ENDPOINT, headers=headers, json=pixel_params)
print(pixel_response.text)

# Update pixels

date = today  # Date to update

UPDATE_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_UNAME}/graphs/{graph_id}/{date}"

update_params = {
    'quantity': '5'
}

update_response = requests.put(url=UPDATE_ENDPOINT, headers=headers, json=update_params)
print(update_response.text)

# Delete pixels

DELETE_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_UNAME}/graphs/{graph_id}/{date}"

delete_response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
print(delete_response.text)
