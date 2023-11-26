import responses
import requests

API_KEY = 'RGAPI-474bc7c7-ca30-4877-832e-f065c0d18ea3'

URL = "https://americas.api.riotgames.com/riot"

headers = {
    "X-Riot-Token": API_KEY
}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print("Request failed with status code:", response.status_code)