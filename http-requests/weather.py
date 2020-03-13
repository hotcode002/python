import requests
import json

url = 'https://api.openweathermap.org/data/2.5/weather'

params = {
    'appid': '37a81ae1e682ac417883b0a3727080a6'
}

params["zip"] = "500050,in"
try:
    response = requests.get(url, params=params, timeout=10)
    print(response.url)
    if response.status_code == 200:
        json = response.json()
        desc = json["weather"][0]["description"]
        name = json["name"]
        print("The weather at ", name, " is ", desc)
    else:
        print("error")
except Exception as e:
    print("Exception occured ,", e)
