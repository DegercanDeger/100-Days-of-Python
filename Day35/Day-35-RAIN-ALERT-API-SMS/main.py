import os
import requests
from twilio.rest import Client

api_key = "3a3a0472f911c56c02bdd1e8072fb77b"
Weather_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = 'AC7b0443a09c90209223eea55c43f79d07' 
auth_token = 'c8b31194cdccda612eb272d154c0128e' 
weather_parametres= {
    "lat": 35.689487,
    "lon": 139.691711,
    "appid":api_key,
    "exclude": "current,minutely,daily"
}
response=requests.get(Weather_Endpoint, params=weather_parametres)
response.raise_for_status()
weather_data = response.json()
weather_sliced = weather_data["hourly"][:12]

will_rain= False
for hour in weather_sliced:
    condition = hour(["weather"][0]["id"]) # Amazing Example For JSON looping...
    if int(condition) < 700:
        will_rain = True
if will_rain:
    #print("Bring an umbrella") # It will not repeteadly print will rain.
    client = Client(account_sid,auth_token)
    message = client.messages \
                .create(
                     body="Selamun Aleykum Baba, Bu mesaji sana kod yazarak yolladim. Eger olduysa beni ara! Ben Can",
                     from_='+905326015927',
                     to='+905424424020'
                 )

print(message.sid)    
#print(weather_data["hourly"][0]["weather"][0]["id"]) # KEY ALMA VE VALUE ALMA SIRASIYLA




# TWILIO RESTRICTS MY ACCOUNT MAYBE BECAUSE I AM IN TURKEY.

