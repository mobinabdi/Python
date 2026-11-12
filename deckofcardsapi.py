import requests

response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

print(response.text)