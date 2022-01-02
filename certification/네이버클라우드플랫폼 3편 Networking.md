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
#### IP주소범위 <br>
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
Classic에서는 포트포워딩을. 통해 서버에 접근 SSL VPN으로 서버접근했다면 VPC에서는 Public Subnet 내에 공인 IP를 부여한 서버에 대해서만 접근 가능하다.<br><br>


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

또한 Load Balancer는 모니터링이 가능하다. 서버모니터링과 마찬가지로 기간선택에 따라 모니터링 정보수집가능.<br> 
마지막으로 여러개의 로드밸런서 규칙을 동시에 설정할수있어서 규칙설정시에 포트를 다른 로드밸런서의 규칙의 포트와 다르게 설정해야한다.<br><br>


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
