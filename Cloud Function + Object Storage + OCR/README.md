# Cloud Function + Object Storage + OCR

## 아키텍처 살펴보기

원하는 구조 : 오브젝트 스토리지에 주민등록증(.jpg)이 들어오면 Cloud Function에서 해당 주민등록증을 OCR 분석하여 결과까지 도출한다.</br>
필요한 서비스 : 오브젝트 스토리지 + Cloud Function + OCR</br>

1) Object Storage
오브젝트 스토리지의 경우 Cloud Funtion과 연결하기 위한 버킷을 하나 생성하였다. 추후 Cloud Function과 연계<br>
나는 object-storage-serverless라는 버킷명으로 만들었고 아래 그림과 같이 이미지들이 추가되면 Cloud Function이 동작하면서 OCR으로 이미지를 TEXT로 출력할것이다<br>
![zz](https://postfiles.pstatic.net/MjAyMTEyMjRfMTcg/MDAxNjQwMzM3MzA0MzE3.rJCzy2nVRPBRt6_qHXvv10a3tAy2vmJut5Nyrgga1jgg.g-5yiVay0e9u30impbFCbCvypYdcXLqbR0j6OXyLR7wg.PNG.mk_crew/%EC%98%A4%EB%B8%8C%EC%A0%9D%ED%8A%B8.png?type=w966) </br></br>


2) OCR
OCR의 경우 General / Template 중에서 주민등록증에 특화된 Template을 선택하였다<br>
둘리 템플릿을 예시로 하나의 템플릿을 생성하였고 배포 및 테스트도 진행을 하였다.<br>
아래 그림은 배포결과를 확인할수있다.<br>
![zz](https://postfiles.pstatic.net/MjAyMTEyMjRfOTcg/MDAxNjQwMzM3MzA3MTQ2._HY-HdyS3oLQAf9GhA7quSpr-D1jsgemQg5JOUogEBYg.C0kkZLQhB443IgGHbCNQkIWrd6L3_Vzkc9_oltxpS1Qg.PNG.mk_crew/dole2.png?type=w966) </br></br>

그리고 Cloud Function의 Action Code와 연동하기위한 OCR Secret Key 값과 URL , Template ID 를 확인한다.</br>
해당 값들은 action_sample.py 의 직접입력 부분에 직접 입력하면된다.</br>

3) CLOUD Function
1번, 2번을 통해서 Cloud Function을 실행하기위한 준비물들은 다 갖췄다.
이제 오브젝트 스토리지에서 이미지가 들어오면 트리거를 발동시켜야한다.</br>
또한 트리거가 발동하면 트리거안에 액션이 발동되어야한다.</br>

트리거가 발동하면 해당 이미지의 Json 형식의 파라메터들을 출력한다.</br>
아래 그림은 트리거를 수행한 결과이다.</br>
![zz](https://postfiles.pstatic.net/MjAyMTEyMjRfMjkw/MDAxNjQwMzM3MzA1MDYw.81f2LSXie00kJFhxU9fk6TsOay2SXTxuRtnda348t7Qg.25hHRPrjKKn_8HsckqyAExpGf7B7QMLW29_UNwdez8Ag.PNG.mk_crew/%ED%8A%B8%EB%A6%AC%EA%B1%B0_%EA%B2%B0%EA%B3%BC.png?type=w966) </br></br>

출력 결과를 바탕으로 Action 에서 action_sample.py 는 해당 key값들을 바탕으로 OCR을 수행한다.
OCR을 수행한 결과는 아래 그림과 같다.</br>
![zz](https://postfiles.pstatic.net/MjAyMTEyMjRfMjI2/MDAxNjQwMzM3MzA0NzMy.1u-fWPiGzXSrbcCzxj2e6dBlbvU-EjtMnY9tZN3ZFQwg.lqsGh2HIajAzzsXkJpUFxcIduYt0496TGoDgSLge9Zkg.PNG.mk_crew/%EA%B2%B0%EA%B3%BC.png?type=w966) </br></br>


## Cloud Function
네이버클라우드플랫폼의 대표적인 Serverless 상품이다.<br>
사용자는 인프라의 관리 부담없이 로직을 분산된 클라우드 환경에서 동작하고 결과를 반환한다.<br><br>

순서 : Action 생성 --> Trigger 생성 --> Action & Trigger 연결 --> 실행결과 확인 <br>

자세한 사용 설명서 확인하기 : <https://guide.ncloud-docs.com/docs/compute-compute-15-1>


## Object Storage
Object Storage는 사용자가 언제 어디서나 원하는 데이터를 저장하고 탐색할 수 있도록 파일 저장 공간을 제공하는 서비스<br>
자세한 사용 설명서 확인하기 : <https://guide.ncloud-docs.com/docs/storage-storage-6-1>

## OCR
CLOVA OCR 서비스를 사용하여 이미지/문서에서 텍스트를 빠르고 쉽게 추출가능<br>
Step 1. 서비스 이용 신청 및 약관 동의<br>
Step 2. 도메인 생성<br>
Step 3. 템플릿 생성<br>
Step 4. 테스트 및 분석<br>
Step 5. 컴포넌트<br>
Step 6. 설정<br>
Step 7. 배포 관리<br>

자세한 사용 설명서 확인하기 : <https://guide.ncloud-docs.com/docs/ocr-ocr-1-1>


## 정리(사용하면서 헷갈렸던 부분들)

Action과 트리거의 디폴트 파라메터 부분이 헷갈렸다.

(1)Action - Default Parameter
(2)Action - Code
(3)Trigger - Default Parameter
(4)Trigger - Event 유형

이렇게 4개로 구분해보자.

(2) 의 경우는 Action에서 직접 코드상에 Default 파라미터를 설정해둘수있다<br>
Default Parameter(1)가 설정되어있지않고 코드의 특정 Key값에 Value가 들어오지않으면 (1)의 값이 출력된다 <br>
(1)이 설정되어있다고하면 (2)이 설정되어있어도 무조건 실행하면 (1)이 출력된다.<br>
우선순위가 (1)이 높으므로 (1)의 입력값을 (2)에서 적용한다.<br>
(3)이 (1)보다 우선순위가 또 높다. 아무리 (1)이 입력되어있어도 (3)이 입력되어있으면 (3)이 출력된다<br>

마지막으로 Custome하게 실행할때 직접입력하는 Key-value값이 가장 우선순위가 높다<br>
따라서 우선순위는 다음과 같다.<br>

직접 입력 > 트리거 디폴드 값 > 액션 디폴드 값 > 코드 값
ex)코드값이 적혀있어도 액션 디폴드값이 적혀있으면 액션 디폴드값으로 출력<br>
ex)액션 디폭드값과 코드값이 적혀있어도 직접입력하면 직접입력값 출력<br>
