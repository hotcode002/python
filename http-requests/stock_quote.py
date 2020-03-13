import requests
import json

url = 'https://api.worldtradingdata.com/api/v1/stock'

params = {
    'api_token': '2KBRjSLj5bOvtuLxfGBuUBESucoZLTGPSYxbqFgbMAoE7hfKq60xXGpAsCIj'
}

params["symbol"] = "ABB"
try:
    response = requests.request('GET', url, params=params, timeout=10)
    if response.status_code == 200:
        json = response.json()
        print(json["data"][0]["price_open"])
    else:
        print("error")
except:
    print("Exception occured")
