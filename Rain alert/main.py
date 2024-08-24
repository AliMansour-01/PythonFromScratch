import requests
from twilio.rest import Client


MY_LATITUDE = 49.887951
MY_LONGITUDE = -119.496010
api_key = "API-KEY" #Enter your API key
account_sid = "" #Enter your twilio account_sid
auth_token = "" #Enter your twilio auth_token


parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": api_key,
    "cnt": 4
}

will_rain = False
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", parameters)
data = response.json()
#weather = data["list"][0]["weather"][0]["id"]

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain",
        from_="", #Enter your twilio acc number
        to="" #Enter number you want the sms to recieve
    )
    print(message.status)