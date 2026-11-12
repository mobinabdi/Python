import requests
def send_sms():
    API_Key = "71674A644B79367A633954504C41452F52596C53684C746B6332506A6E73376B7154526C464F4F523275513D"
    url = "https://api.kavenegar.com/v1/%s/sms/send.json" % API_Key
    print(url)

response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

deck_id  = response.json()['deck_id']
if deck_id != '':
    send_sms()