import requests

client_id = ""
client_secret = ""

url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"

text = "원하시는 텍스트를 입력해주세요."

# ko : 한국어
# en : 영어
# zh-CN : 중국어 간체
# zh-TW : 중국어 번체
# es: 스페인어
# fr: 프랑스어
# vi: 베트남어
# th: 태국어
# id: 인도네시아어


# body
val = {
    "source": 'ko',
    "target": 'en',
    "text": text
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