---
title:  "네이버클라우드플랫폼 AI/Application"
excerpt: "네이버클라우드플랫폼 파헤치기 9편 "
toc: true
toc_sticky: true

categories:
  - cloud
tags:
  - 네이버클라우드플랫폼
  
last_modified_at: 2021-03-06T08:07:00-08:00
---

# AI & Application
네이버클라우드플랫폼의 AI서비스는 파파고와 클로바가 대표적이다.<br>
AI플랛폼인 Clova, 번역서비스인 Papago, 딥러닝을 위한 Tensorflow탑재된 서버 이미지가 제공된다.<br><br>

Application의 경우 네이버에서 사용하는 기술과 서비스를 API로 제공한다.<br>
Geolocation, Maps,nShortURL,SENS,Search Trend등이 제공된다.<br>
네이버 통합검색 서비스를 통해 수집되는 검색어 통계를 다양한 기준으로 조회하고 활용가능하다.<br>
대량 메일 발송을 위한 Outbound Mailer도 존재한다.<br>
고객대응에 활용할수있는 챗봇도 사용가능<br>
그럼 하나씩 서비스들을 살펴보도록 하자.<br><br>

### GeoLocation
<CLASSIC / VPC 환경에서 공통으로 사용><br>
사용자IP를 통해서 위치 정보를 제공하는 국내 유일의 서비스<br>
고객서버에서 질의한 IP주소에 따른 지역정보 DB를 검색해 국가,시/군/구 좌표정보를 전달한다.<br>
접속IP를 기반으로 동까지 확인이 가능하다.<br>

### SENS
<CLASSIC / VPC 환경에서 공통으로 사용><br>
SMS + APP PUSH를 손쉽게 이용가능<br>
웹을 통해서 혹은 API를 이용해 다수에게 SNS,PUSH가 발송가능하다.

### Outbound Mailer
<CLASSIC / VPC 환경에서 공통으로 사용><br>
대량 메일 발송을 위한 메일 발송상품
광고 메일 발송을 위한 템플릿 기능, 법적인 기능제공<br>
템플릿에는 네이버메일과 동일한 입력기인 스마트에디터를 제공하고 치환 태그기능을 통해 변수사용이 가능하다.<br>

### 챗봇(Chatbot)
<CLASSIC / VPC 환경에서 공통으로 사용><br>
주문시스템과 같은 고객 대응을 로봇으로 대체하는 상품<br>
학습을 통해 적절한 답변을 자동화,CSR,CSS와 연동가능하고 음성채팅까지 지원한다.<br>

아래부터 설명할 내용은 클로바더빙 웨비나를 시청해보면 훨씬더 손쉽게 전체적인 이해가 가능하다.<br>
나의 인턴 첫 외부노출자료이기도하다(ㅎㅎ)...<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Gy0Jt12FfgE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### CSR(Clova Speech Recognition)
<CLASSIC / VPC 환경에서 공통으로 사용><br>
음성을 텍스트로 변환<br>
국내에서 가장 높은 한국어 인식률<br>
안드로이드와 IOS둘다지원을하고 REST API를 제공한다. <br>
마지막으로 한국어,영어, 일어,중국어를 제공한다.<br>

### Clova Speech
<CLASSIC / VPC 환경에서 공통으로 사용><br>
긴 음성을 인식하고 텍스트로 추출<br>
클로바는 한국어와 관련된 AI서비스에 강점을 가지고있다.<br>
높은 성능의 한국어 장문 딕테이션과 미디어 인식에 강하다.<br>
또한 전화망 음성인식이 가능하고 현재도 지속적으로 Training하여 성능이 향상되고있다.<br>

### Clova Voice
<CLASSIC / VPC 환경에서 공통으로 사용><br>
총 29가지 음성을 제공한다.<br>
최대 1000글자 변환이 가능하고 Volume, Speed,Pitch, Emotion등 감정 파라메터도 제공한다.<br>
Wav포맷의 경우 샘플링 Rate를 지원한다.<br>

### Clova Dubbing
<CLASSIC / VPC 환경에서 공통으로 사용><br>
컨텐츠에 나레이션 추가하는 기능<br>
최대 500MB, 20분 이내 영상에 대해 더빙이 가능하다.<br>
자세한 내용은 클로바 더빙 웨비나 동영상을 확인하길바란다.<br>

### Clova Face Recognition
<CLASSIC / VPC 환경에서 공통으로 사용><br>
입력된 Vision 데이터를 통해 얼굴을 인식하고 관련된 정보를 제공한다.<br>
크게 두가지 서비스를 제공한다. 1. 유명인 얼굴인식과 2. 얼굴감지 <br>
국내에서 가장 뛰어난 유명인 얼굴인식과 정확한 얼굴감지기능을 네이버 기술력으로 제공한다고한다.<br>
AI기술인 머신러닝을 사용하여 지속적으로 학습중이다.<br>
마지막으로 RESTful API를 제공하여서 쉽게 적용이가능하다.<br>

### Clova OCR
<CLASSIC / VPC 환경에서 공통으로 사용><br>
지정된 템플릿에 맞추어 데이터를 추출하고 데이터베이스화할수있다.<br>
Classify--> Pre-process--> Area Detection -->Text Recognition--> Test/Output 형태의 Process이다.<br>
예전에 개발회사에서 인턴을할때 해당 OCR를사용하여 세금계산서같은 일정한 형식의 문서에 대한 텍스트추출을 통해 현업의 실무자들이 훨씬 효율적으로 업무를 진행할수있었던 기억이있다.<br>

### Papago NMT(Neural Machine Translation)
<CLASSIC / VPC 환경에서 공통으로 사용><br>
통계기반번역으로 번역할 언어의 종류를 자동 탐지한다.<br>
학습을 톨해 성능이 높아지고있으며 Rest API를 제공한다.<br>
자연스러운 번역기술을 제공하고 영어 일어 중국어를 제공한다.<br>

### Pose Estimation
<CLASSIC / VPC 환경에서 공통으로 사용><br>
이미지내의 주요 신체 영역을 인식하고 해당 영역을 좌표로 변환한다.<br>
이미지를 분석하여 신체영역 좌표를 결과값으로 제공한다.<br>
RestFUL API방식이며, 이미지는 2MB이하로제한된다.<br>

###  Object Detection
<CLASSIC / VPC 환경에서 공통으로 사용><br>
이미지내의 객체를 탐지하고 객체를 분석한다.<br>
객체를 탐지하여 객체의 이름,바운딩박스, 팀지 정확률을 제공한다.<br>
RESTful API방식으로 제공을하고 이미지는 2MB이하이다.

### Search Trend
네이버통합검색 서비스 조회 결과에 대한 통계 API
특정 키워드의 검색량을 기간별로 확인가능하다.<br>
연령별,성별,검색 시 사용 디바이스별 세분화 조회가 가능하다<br>
키워드 및 세분화 조회를 선택하여 REST API로 전달하면 통계 결과를 리턴한다.<br>
직관성을 위해 요청된 기간 중 검색 횟수가 가장 높은 시점을 100으로 둔다.<br>

### nShortURL
길고 복잡한 URL을 간단하고 짧게 변경하는 API<br>
긴 URL을 단축하여 글자 수 제한이 있는 SMS를 전송하거나 SNS를 이용시 사용한다.<br>
최근 유해 정보를 기반으로, 유해성이 필터링된 URL만 생성가능하다.<br>
REST API를 제공하고 QR코드 이미지를 무료로 함께 생성한다.<br>

