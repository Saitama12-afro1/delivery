import json
import requests
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDQ2NzMsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IlNoYWhtYXRpc3RQaXRvbmlzdCJ9.DVMdTenDBFY0xfUDaRez-V_rEJTD9N5dKZdZSzl64W4"
url = "https://probe.fbrq.cloud/v1/send/12"

json_body = json.dumps({
  "id": 1,
  "phone" : 124165,
  "text": "113143"
})

responce = requests.post(url=url,json=json_body)

print(responce.text)