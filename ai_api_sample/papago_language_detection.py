import requests

client_id = ""
client_secret = ""

url = "https://naveropenapi.apigw.ntruss.com/langs/v1/dect"

val = {
    "query": "지금 이 문장은 어떤 언어인지 알려줘"
}


headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret
}

response = requests.post(url,  data=val, headers=headers)
rescode = response.status_code

if rescode == 200:
    print(response.text)
else:
    print("Error : " + response.text)