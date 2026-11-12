import requests
def send_sms(deck_id):
    API_Key = "71674A644B79367A633954504C41452F52596C53684C746B6332506A6E73376B7154526C464F4F523275513D"
    url = "https://api.kavenegar.com/v1/%s/sms/send.json" % API_Key
    payload = {"receptor": "09185165849","message": 'Code: %s' % deck_id}
    response = requests.post(url,data=payload)
    print(response)

response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

deck_id  = response.json()['deck_id']
if deck_id != '':
    send_sms(deck_id)