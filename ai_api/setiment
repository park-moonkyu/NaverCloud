import sys
import requests
import json
import cgi, os
import codecs


client_id = ""
client_secret = ""


#코덱변환 한글 입력
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# cgi 형식 확인
# cgi.test()

form = cgi.FieldStorage()
content = form['content'].value

data = {
    "content" : content
}


url = "https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze"

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": 'application/json'
}


# print(json.dumps(data, indent=4, sort_keys=True))

response = requests.post(url, data=json.dumps(data), headers=headers)

## 결과 도출용으로 활용 가능
sentiment_data = response.json().get('document')
sentiment=sentiment_data.get('sentiment')
sentiment_per=sentiment_data.get('confidence')

rescode = response.status_code
if rescode == 200:
    print(response.text)
else:
    print("Error Code:" + rescode)