import requests

response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

deck_id  = response.json()['deck_id']
if deck_id != '':
    draw = requests.get("https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2")