---
title:  "네이버클라우드플랫폼 Networking - LoadBalancer"
excerpt: "네이버클라우드플랫폼 파헤치기 5편 "
toc: true
toc_sticky: true

categories:
  - cloud
tags:
  - 네이버클라우드플랫폼
  
last_modified_at: 2021-02-17T08:07:00-08:00
---

## 로드밸런서(Load Balacner)
### Target Group
요청을 처리할수있는 대상에 대한 집합<br>
동일한 VPC내에 있는 서버들에 대한 타겟그룹 생성가능<br>
타겟 그룹안에 있는 서버를 다른 타겟그룹에 속하게 할 수 있지만 타겟 그룹을 다수의 로드밸런서에 연결할수없다.<br>
서비스를 수행하는 대상의 프로토콜에 따라 L4와 L7으로 구분<br>
헬스체크 주기(5~300초) 및 임계값 설정가능<br>
기본은 Round Robin설정이지만 Sticky,ProxyProtocol설정변경은 생성 이후에 진행<br>

### 프로토콜
TCP: Network Load Balancer<br>
Proxy_TCP : Network Proxy Load Balancer <br>
HTTP : Application Load Balancer<br>
HTTPS: Application Load Balancer<br>
<br><br>

부하처리 성능에 따라 Small/Medium/Large 선택가능하며 각각. 초당 연결수 기준 최소 30,000/60,000/90,000 분산처리 보장<br>

### 로드밸런싱 알고리즘
Round Robin : 클라이언트에서 요청이 오면 서버에 1개씩 분배하는 방식<br>
Least Connection : 클라이언트 연결이 제일 적은 서버에게 새로운 커넥션을 분배하는 방식<br>
Source IP Hash : 클라이언트 IP에 대한 해시테이블을 가지고 클라이언트 IP에 맵핑되는 서버에 새로운 커넥션을 분배<br>

### 로드밸런서 종류
#### 애플리케이션 로드밸런서 
HTTP,HTTPS를 사용하는 웹 애플리케이션에 보다 유연한 구성이 가능<br>
고정 IP3제공하고 URL기반의 분기가 가능하다 마지막으로 3개의 알고리즘을 제공한다.<br>
웹 기반의 콘솔에서 SSL인증서를 추가할수있다.<br>
L7기능을제공하여서 HTTP/HTTPS 트래픽에 대해서 패킷 헤더를 확인하여 Application 레벨에서의 분기처리를 제공한다.<br>
#### 네트워크 로드밸런서
고성능의 분산처리 가능<br>
Client IP가 그대로 로깅<br>
알고리즘은 Source IP Hash ,Round Robin만 제공<br>
TCP레벨 고성능 분산처리로 초당 연결 수 기준 최소 100,000개에서 최대 400,000개 까지 성능보장<br>
또한 트래픽 분배만 수행하고 고객 서버에서 직접 응답하는 기능(DSR)을 구현하여 보다 빠르고 효율적인 서비스 이용<br>
#### 네트워크 프록시 로드밸런서 
Classic과 유사한 로드밸런서<br>
프록시방식의 통신을 제공하여 세션 유지가 필요한 TCP기반 애플리케이션에 이용할수있다.<br>
또한 애플리케이션 로드밸런서와 동일한 부하분산 알고리즘 적용가능하다.<br>
웹 기반의 콘솔에서 SSL인증서를 추가할수있다.<br>
<br>

또한 Load Balancer는 모너터링이 가능하다. 서버모니터링과 마찬가지로 기간선택에 따라 모니터링 정보수집가능.<br> 마지막으로 여러개의 로드밸런서 규칙을 동시에 설정할수있어서 규칙설정시에 포트를 다른 로드밸런서의 규칙의 포트와 다르게 설정해야한다.<br>
