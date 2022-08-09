import json
import requests
import pprint

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDQ2NzMsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IlNoYWhtYXRpc3RQaXRvbmlzdCJ9.DVMdTenDBFY0xfUDaRez-V_rEJTD9N5dKZdZSzl64W4"
url = "https://probe.fbrq.cloud/v1/send/1"

json_body = json.dumps({
  "id": 1,
  "phone" : 0,
  "text": "113143"
})
headers = {}
headers["accept"] = "application/json"
headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTEyNDQ2NzMsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IlNoYWhtYXRpc3RQaXRvbmlzdCJ9.DVMdTenDBFY0xfUDaRez-V_rEJTD9N5dKZdZSzl64W4"
headers["Content-Type"] = "application/json"

data = """
{
  "id": 2,
  "phone": 32,
  "text": "string"
}"""
responce = requests.post(url=url,data=json_body,headers=headers)

pprint.pprint(responce.text)