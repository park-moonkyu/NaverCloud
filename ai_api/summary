
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
title= form['title'].value
content = form['content'].value

data = {
    "document": {
        "title": title,
        "content": content
        },

    "option": {
        "language": "ko"
    }
}

url = "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": 'application/json'
}


# print(json.dumps(data, indent=4, sort_keys=True))

response = requests.post(url, data=json.dumps(data), headers=headers)
summary_data = response.json()
