---
title:  "네이버클라우드플랫폼 Security/Media "
excerpt: "네이버클라우드플랫폼 파헤치기 11편 "
toc: true
toc_sticky: true

categories:
  - cloud
tags:
  - 네이버클라우드플랫폼
  
last_modified_at: 2021-03-06T08:07:00-08:00
---

## Site Safer, APP Safer
### Site Safer
고객의 웹페이지에 악성코드가 있는지 주기적으로 검사<br>
NCP외부 IP대역도 점검 가능<br>
행위 기반탐지를 한다.<br>
### APP Safer
고객의 APP 실행 모바일 환경에 대한 보안 위협 여부를 실시간으로 탐지한다.<br>
치팅 프로그램, 핵 등으로 APP 무결성 검사<br>
<Classic/VPC공통 서비스><br>
<br>

## File Safer
업로드/다운로드 되는 파일의 악성코드 여부를 탐지<br>
고객의 웹페이지에 업/다운로드 되는 파일에 대한 체크<br>
악성코드 여부를 신속하고 정확하게 탐지<br>
<Classic/VPC공통 서비스><br>
<br>
## Web Security Checker
고객의 웹사이트 보안 취약점 진단<br>
고객의 웹페이지에 취약점이 있는지 없는지 체크한다.<br>
취약점에 대한 진단뿐 아니라 대응방안도 함께 제공한다.<br>
현재 18가지 주요 웹 취약점에 대해 점검 가능하다.<br>
<Classic/VPC공통 서비스><br>
<br>
## App Security Checker
고객의 모바일 App 보안 취약점 진단<br>
고객의 모바일 App을 분석하여 자동으로 보안 취약점을 점검할 수 있는 서비스로 진단 리포트 제공<br>
모바일 App 출시전 사용하여 App취약점 체크할 수 있는 상품<br>
<Classic/VPC공통 서비스><br>
<br>
## Certificate Manager
SSL 인증서 등록 및 관리의 통합<br>
네이버 클라우드 플랫폼의 연계상품(Load Balancer, CDN+, Image Optimizer)에서 사용할 인증서 등록가능<br>
인증서의 만료 예정일 한달 전부터 정기적으로 알람 메일과 SMS발송<br>
<Classic/VPC공통 서비스><br>
<br>

## Security Monitoring
네이버클라우드플랫폼의 향상된 보안 부가상품<br>
기본적으로 IDS 이벤트를 탐지하고 Anti-Virus를한다<br>
Managed로는 IDS이벤트 탐지를하고 DDos이벤트탐지를하며 IPS이벤트 탐지를한다. <br>
<Classic/VPC공통 서비스><br>
<br>
## SSL VPN
__SSL VPN을 통한 서버 접속<br>__
10대역의 28bit VPN IP대역 제공(Classic)<br>
VPC 내의 Subnet에 생성(VPC)<br>
SSH,RDP와 같은 포트는 외부에서 접근할 수 없도록 ACG에서 차단<br>
ACG에 VPN IP대역에 대해서 접근 가능하도록 설정하여 서버를 안전하게 관리가능<br>
<Classic/VPC공통 서비스><br>
<br>
__최대 10개 ID생성가능 및 전용 VPN프로그램 설치하여 VPN사용__
클래식의 경우 콘솔에서 최대10개 아이디 생성가능<br>
VPC의 경우 콘솔에서 최대 500개 ID생성가능<br><br>
__1차인증과 2차인증 지원__<br>
아이디 패스워드로 로그인가능한 1차인증<br>
아이디패스워드 뿐만아니라 SMS/Mail의 OTP를 입력해야하는 2차인증<br>
<Classic/VPC공통 서비스><br>
<br>
## WebShell Behavior Detector
__외부로부터의 웹 쉘 공격을 실시간 탐지__<br>
Agent기반 탐지 시스템<br>
행위기반 실시간 웹셀 탐지를 비롯하여 알려지지않은 의심스러운 패턴감지<br>
웹셀 의심 파일을 격리 혹은 복구 가능 <br>

## Live Station
__실시간방송을 위한 플랫폼__<br>
트랜스코딩을 통해 여러 화질로 변환후 송출<br>
스트림상태를 볼수있는 모니터링 기능 제공<br>
썸네일 이미지 추출가능<br>
타임머신기능으로 놓치지않고 라이브 방송 서비스 구현 가능<br>
CDN 연동을 통해 안정적인 송출가능<br>
<Classic/VPC공통 서비스><br>

## VOD Station
__VOD 스트리밍 플랫폼__<br>
Object Storage에 보관된 영상 파일을 이용하여 스트리밍 서비스 제공<br>
CDN연동을 통해 안정적인 송출이 가능하다<br>
Live Station, VOD Transcoder 와 연동하여 사용이 가능하다<br>
DRM 적용기능을 제공한다.<br>
<Classic/VPC공통 서비스><br>

## VOD Transcoder
__고품질 저비용의 클라우드 미디어 파일 변환 서비스__<br>
VOD Transcoder는 미디어 원본 파일을 모바일 PC등 다양한 디바이스에서 다양한 화질로 시청할 수 있도록 변환해주는 클라우드 기반의 미디어 서비스<br>
시중에서 사용되는 모든 입력포맷 지원 및 높은 인코딩 성공률<br>
인터넷라이브생중계를 할수있는 Live Transcoder, 대용량의 트래픽을 처리할수있는 CDN과 결합하여 통합서비스 구현가능<br>
<Classic/VPC공통 서비스><br>

## Image Optimizer
__이미지를 다양한 사이즈로 변환하여 CDN을 통해 제공__<br>
이미지를 Object Storage에 업로드하면 미리 설정된 룰에 맞추어 이미지 변환<br>
이미지는 CDN+ 를 통해 제공되고 리사이즈 크롭시 자동회전 및 얼굴인식 기능이 제공된다<br>
<Classic/VPC공통 서비스><br>

## Video Player
__NCP 미디어 서비스에 최적회된 비디오 플레이어__<br>
네이버 동영상플레이어엔진을 사용하고 향후 DRM및 커스터마이징 기능을 제공예정이라고한다.<br>
사용자가 커스텀 플레이어를 생성할수있고 커스텀 플레이어는 오브젝트 스토리지에 저장된다.<br>
<Classic/VPC공통 서비스><br>

## Workplace
__인사,회계,그룹웨어 SaaS__
워크플로우,인사,회계시스템에 사내 메신저, 게시판, 조직도 기반 주소록,메일,캘린더,사내공유폴더까지 기업에서 필요로하는 백오피스 시스템을 SaaS로 제공한다.<br>
또한 모바엘 환경에 최적화 된 App도 제공한다.<br>
<Classic/VPC공통 서비스><br>


## NAVER WORKS
__네이버가 만든 업무용 협업 도구__
전네이버가 네이버웍스를 사용하고 사용해보면 정말 쉽고 편리하다.<br>
메신저를 중심으로 메일,캘린더,주소록,설문,드라이브 등 업무에필요한 다양한 기능을 제공한다.<br>
필요한 기능 및 사용인원에 따라서 Free/Lite/Basic/Premium 중 상품선택이 가능하다.<br>
<Classic/VPC공통 서비스><br>
