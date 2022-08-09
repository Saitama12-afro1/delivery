import requests
responce = requests.post("https://probe.fbrq.cloud/docs#/send/sendMsg")

print(responce.headers)