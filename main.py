import os

import requests
from twilio.rest import Client

api_key = os.environ.get("API_KEY")


parameters = {
    "lat":os.environ.get("LAT"),
    "lon":os.environ.get("LON"),
    "appid":api_key,
    "cnt":4
}

weather_data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params =parameters)
data = weather_data.json()
will_rain = False
auth_token = os.environ.get("AUTH_TOKEN")
auth_sid = os.environ.get("AUTH_SID")
from_no = os.environ.get("FROM_NO")
my_number = os.environ.get("MY_NUMBER")
id_list = []
for i in range(0,4):
     ids = data["list"][i]["weather"][0]["id"]
     id_list.append(ids)
for item in id_list:
    if item<700:
        will_rain = True
if will_rain:
    client = Client(auth_sid,auth_token)
    message = client.messages.create(
        body = "Bring an Umbrella",
        from_=from_no,
        to = my_number

    )
    print(message.status)



