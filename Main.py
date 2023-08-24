
import requests
import json

url = "http://api.weatherapi.com/v1/current.json"
api_key = "15ad903d52214596b61233325211509"

while(True):
    city = input("City = ")

    forecast = requests.get(url, params={
        "key":api_key,
        "q":city,
        "lang":"tr" 
    })

    result = forecast.json()

    latitute = result["location"]["lat"]
    longtitute = result["location"]["lon"]
    local_time = result["location"]["localtime"]
    tempsure = result["current"]["temp_c"]
    text = result["current"]["condition"]["text"]

    print(f"{city} is {tempsure}C {text}\n{local_time}\n{latitute}-{longtitute}")