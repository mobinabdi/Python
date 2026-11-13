import requests

API_Key = "ONjDcWL6udqe0dYYfyUiSMDxe2SglEABWwZWzCFGcPlKPTHv"
text  = '''سلام پیامک تست'''
url = "https://api.sms.ir/v1/send/verify"
# from kavenegar import KavenegarAPI, APIException, HTTPExc'eption
def send_sms(mobile,text):
    headers = {
        "Content-Type": "application/json",
        "Accept": "text/plain",
        "x-api-key": API_Key,
    }
    payload = {
        "mobile": mobile,
        "templateId": text,
        "parameters": [
            {"name": "Code", "value": deck_id}
        ],
    }
    r = requests.post(url,json=payload,headers=headers)
    print(r.status_code,r.text)

response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

deck_id  = response.json()['deck_id']
if deck_id != '':
    mobile = '09185165849'
    send_sms(mobile,text)