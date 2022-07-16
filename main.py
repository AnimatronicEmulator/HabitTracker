import requests
import config
import datetime

USERNAME = config.username
TOKEN = config.token

current_date = (datetime.datetime.now()).strftime("%Y%m%d")

# VVVV CHANGE BELOW VVVV
# Note that the documentation specifies int or float for quantity, but kept getting error for not using string.
minutes_spent_programming = "180"
target_graph_id = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_config = {
    "id": "graph1",
    "name": "Python Programming Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "momiji",
}
pixel_config = {
    "date": current_date,
    "quantity": minutes_spent_programming
}

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{target_graph_id}"

# Creating account
# response0 = requests.post(url=pixela_endpoint, json=user_params)
# print(response0.text)

# Creating a new graph
# response1 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response1.text)

# Creating a pixel in our graph
response2 = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response2.text)
