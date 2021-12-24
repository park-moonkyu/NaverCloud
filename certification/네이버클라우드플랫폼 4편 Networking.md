---
title:  "네이버클라우드플랫폼 Networking - VPC"
excerpt: "네이버클라우드플랫폼 파헤치기 4편 "
toc: true
toc_sticky: true

categories:
  - cloud
tags:
  - 네이버클라우드플랫폼
  
last_modified_at: 2021-02-17T08:07:00-08:00
---

##  Networking
VPC기준으로 설명<br>
__외부와의 통로, 내부와의 통로 뿐만아니라 DNS,CDN과 같은 다양한 서비스를 제공<br>__
유입되는 네트워크 트래픽을 백엔드 서버로 분기하기 위한 로드밸런서 사용<br>
네엄서버 제공하는 DNS<br>
요청 사용자에 가장 가까운 엣지서버에서 캐싱된 파일을 제공하여 원본부하를 낮출 수 있는 CDN <br>
Site to Site 연결을 위한 IPSEC VPN<br>
비공인 IP를 가진 다수의 서버에게 단일 공인IP를 이용한 외부 접속을 제공하는 NAT Gateway제공<br>
글로벌 네트워크 트래픽을 백엔드 서버로 분기하기위한 GRM(Global Route Manager)<br>

### VPC
VPC의 경우 기존 Classic과 구분되어 VPC와 Classic간의 사설 통신 및 상품 이용은 불가<br>
IP 대역을 설정하는 VPC<br>
네트워크 Segment를 구성하는 Subnet<br>
Subnet단위로 통신을 제어하는 Network ACL<br>
VPC간 사설 통신을 가능하게하는 VPC Peering<br>
VPN/전용선 연결시 통신을 가능하게 하는 Route Table/ Virutal Private Gateway<br>
<br>
네이버클라우드플랫폼의 경우 한국리전 민간,금용 클라우드에 VPC적용<br>
계정당 최대 3개의 VPC가 생성가능하다.<br>
#### IP주소범위 
10.0.0.0/8 , 172.16.0.0/12, 192.168.0.0/16 중에 선택<br>
최소 /28 ~ 최대 /16까지 Netmask 생성이 가능하다.<br>
Subnet을 이용하여 VPC안에서 Segment 생성관리가 가능하다.<br>

#### Peering
VPC간 연결을 위한 네트워크 구성<br>
내 VPC간 연결뿐만 아니라 다른계정과의 VPC연결도 가능<br>
타계정 VPC연결시 로그인 ID,VPC ID, VPC명 입력 필요<br>

### VPC-ACG&NACL
Network Access Control List의 약자로 VPC의 보안 강화요소<br>
NACL이 Subnet에 적용되어 외부에서 접속시 NACL룰 검사가 먼저 진행<br>
Allow / Deny 모두 설정 가능, 상태 비저장 방식<br><br>
(ACG) 서버 단위로 적용 // (NACL) Subnet 단위로 적용<br>
(ACG) Allow규칙에 한하여 지원 // (NACL) Allow,Deny 규칙 모두 지원<br>
(ACG) Stateful: Response트래픽 자동 허용 // (NACL) Stateless : Response 트래픽에 대한 Allow 규칙이 추가적으로 필요<br>
(ACG) 모든규칙을 확인하여 판단 // (NACL) 우선순위에 따라 규칙을 반영<br><br>
서버, Subnet에 적용된 ACG,NACL를 다른 ACG,NACL으로 변경가능<br>

#### Subnet
VPC주소 범위 내에서 CIDR 형태로 주소 범위 지정<br>
Zone을 지정할 수 있으며 동일한 Zone내에 여러 Subnet 생성 가능<br>
인터넷과 연결되는 Public Subnet과 폐쇄적인 Private Subnet으로 구분<br>
Public Subnet내에 서버만 Public IP부여가능<br>
VPC당 최대 200개의 Subnet 생성가능<br>
<br>
__Public Subnet__<br>
서버만 위치시킬수 있으며 서버에 공인IP를 부여가능.<br>
__Private Subnet__<br>
서버 혹은 로드밸런서를 위치시킬수 있다.<br>
<br>
Classic에서는 포트포워딩을. 통해 서버에 접근 SSL VPN으로 서버접근했다면 VPC에서는 Public Subnet 내에 공인 IP를 부여한 서버에 대해서만 접근 가능하다.<br>

