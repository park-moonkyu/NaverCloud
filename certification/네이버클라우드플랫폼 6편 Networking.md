---
title:  "네이버클라우드플랫폼 Networking - DNS/CDN"
excerpt: "네이버클라우드플랫폼 파헤치기 6편 "
toc: true
toc_sticky: true

categories:
  - cloud
tags:
  - 네이버클라우드플랫폼
  
last_modified_at: 2021-02-17T08:07:00-08:00
---

## DNS (곧없어지므로 --> GDNS 추천)
도메인 등록서비스 <br>
다양한 레코드 타입을 지원한다. (A,NS,PTR,AAAA,MX,CNAME 등)<br>
등록 도메인으로 인입되는 트래픽을 분기한다.(Round Robin)<br>
등록된 도메인에 대한 헬스체크는 불가하다.<br>

## GDNS
도메인 등록서비스<br>
다양한 레코드 타입을 지원한다. (A,NS,PTR,AAAA,MX,CNAME 등)<br>
Alias기능 제공 및 설정반영단계 추가.<br>
등록 도메인으로 인입되는 트래픽을 분기(Round Robin)<br>
모니터링 기능을 제공한다.<br>

## CDN+, Global CDN
__컨텐츠를 Caching하여 보다 빠르고 안정적으로 사용자에게 전송하는 서비스<br>__
국내 국외 주 서비스 지역에 따른 CDN 상품 분리 제공(CDN+: 국내전용, GCDN: 국외전용)<br>
원본은 NCP오브젝트 스토리지 혹은 커스텀 오리진 서버를 둘수있다.<br>
도메인은 랜덤 CDN도메인 혹은 보유하고있는 도메인 사용가능하다.<br>
지원프로토콜은 HTTP/S<br><br>

__CDN은 그럼 언제필요할까?__<br>
대규모 파일 배포나 이미지 서비스, 동영상 서비스등 대규모 트래픽 발생시<br>
웹서버를 통해 배포하면 웹서버의 용량이 기하급수적으로 커져야한다.<br>
이러한 대규모 트래픽을 효과적으로 대응가능하다.<br><br>

### CDN관련용어 알아보기
#### Purge
CDN 캐시서버에 저장되어있는 콘텐츠를 삭제하는 기능<br>
#### Cache expiry
CDN에서 캐싱된 콘텐츠가 원본서버에서 변경되었는지 여부를 확인하는 주기를 지정<br>
#### Streaming 
네트워크 기반 사용자들에게 멀티미디어 정보를 실시간으로 제공하는 기술<br>
#### Secure Token
토큰 기반의 인증으로 허용된 접근에만 콘텐츠를 전달
#### Ignore Query String
CDN 서비스가 원본서버에 요청할때 ?id=1234와 같이 URL에 포함된 GET파라미터를 제거한 후에 요청
#### Referrer Domain
콘텐츠가 지정된 도메인에만 제공되므로 다른 사이트에서 참조되는것을 방지.
#### Access log
CDN 사용 로그를 확인할수있는 기능, CDN사용 로그를 자신의 파일 스토리지 컨테이너에 약 10분주기로 저장<br>
#### HIT
접속자가 요청한 콘텐츠가 유효한 형태로 CDN캐시서버에 있어 접속자의 요청에 대해서 바로 응답할때 HIT라고함<br>
#### BYPASS
원본서버에 응답헤더에 Set-Cookie헤더가 있거나 Cache-Control에 헤더에 Private, no-cache, max-age=0 등의 내용이 있는 경우 CDN서버에서 캐싱하지않고 접속자에게 전달하는것을 의미한다.<br>

## IPSEC VPN
__고객의 사내망과 NCP간 사설 통신을 위한 IPSEC VPN<br>__
고객의 VPN장비와 NCP VPN장비 간 터널링 연결 제공(통신 방식 호환이 되어야 함)<br>
NCP서버들은 Private Subnet대역(192.168.x.x)으로 통신 필요<br>
BW 최대 30Mbps 제공<br>

## NAT Gateway
### Classic
비공인 IP를 가진 다수의 서버에게 대표 공인IP를 이용한 외부접속을 제공<br>
NAT Gateway를 통해 외부로 접속할때 사용되는 대표 공인 IP는 해당 NAT Gateway만 독점적으로 사용하는 IP<br>
Auto Scaling과 연계된 자동 설정 제공<br>
보안상 다수의 공인IP에 대한 ACL을 오픈할 수 없는 경우 혹은 공인IP 생성 비용 절약 가능<br>
### VPC
Private Subnet에서 외부로의 통신이 필요한 경우, 외부접속을 제공<br>
NAT Gateway를 연결하고, Route Table을 수정하여 외부 접속을 가능하도록 설정할 수 있다.<br>
Private Subnet은 Internet Gateway가없기때문에 외부통신이 불가하다.<br>

## Global Route Manager(GRM)
DNS기반의 다양한 방법을 통해 네트워크 트래픽을 안정적으로 로드밸런싱하는 GSLB상품<br>
로드밸런싱 타입은 4가지 제공(Round Robin, Weighted, GeoLocation, Failover)<br>
IP에 대한 Health Check만 제공<br><br>
