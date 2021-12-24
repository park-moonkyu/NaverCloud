# Cloud Function + Object Storage + OCR


## Cloud Function
네이버클라우드플랫폼의 대표적인 Serverless 상품이다.<br>
사용자는 인프라의 관리 부담없이 로직을 분산된 클라우드 환경에서 동작하고 결과를 반환한다.<br><br>

순서 : Action 생성 --> Trigger 생성 --> Action & Trigger 연결 --> 실행결과 확인 <br>

자세한 사용 설명서 확인하기 : <https://guide.ncloud-docs.com/docs/compute-compute-15-1>


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
