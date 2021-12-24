---
title:  "네이버클라우드플랫폼 Analytcis"
excerpt: "네이버클라우드플랫폼 파헤치기 10편 "
toc: true
toc_sticky: true

categories:
  - cloud
tags:
  - 네이버클라우드플랫폼
  
last_modified_at: 2021-03-06T08:07:00-08:00
---

## Monitoring(모니터링)
클라우드 리소스 상태 모니터링 수행<br>
모든 상품에 대해 모니터링 서비스 제공<br>
기본 : 상품별 모니터링 그래프 확인 가능<br>
상세 : 메트릭에 대한 임계치 설정과 이벤트 발생 시 Alert 기능( SMS/ E-mail )<br>
83개 세부 항목에 대한 모니터링 성능 정보를 수집하며, 그 중 약 60여개의 세부 항목에 대한 이벤트 경보 설정가능<br>

## Cloud Insight
통합 관리 모니터링 서비스<br>
NCP 상품 및 사용자 애플리케이션 성능/운영 지표를 One Page로 통합
네이버클라우드 플랫폼에서 만든 Basic Metric뿐만 아니라, 사용자 설정에 따른 Custom Metric설정 가능<br>
단계별 Event Rule생성과 Event 담당자 지정가능하고 SMS 및 Email 알람가능<br>
유지보수 설정 기능을 통해 실제 장애로 인한 알람과 구분 가능<br>
** VPC 환경에선는 Monitoring 서비스가 사라지고 해당 기능이 Cloud Insight에 편입되었다.<br>

## Sub Account
서브 계정별 역할 부여를 통한 리소스관리<br>
다수의 사용자가 동일한 자원을 이용하고 관리할 수 있도록 역할을 부여한 서브계정을 제공하는 서비스이다.<br>
서브계정이 작업한 모든내역은 Cloud Activity Tracer 상품에서 확인이 가능하다.<br>

## Web Service Monitoring System(WMS)
고객의 웹피이지 품질 측정도구<br>
웹서비스URL을 입력하여 실시간으로 테스트를 진행가능하고 스케줄을 등록하여 반복적 모니터링도 가능<br>
경보 설정을 통해 모니터링 등록된 URL에서 오류가 감지되면 SMS나 EMAIL을 통해 발송가능<br>
시나리오 기반 모니터링을 제공하여, 사용자 이용패턴에 따른 각 기능별 모니터링 수행가능<br>

## Cloud Activity Tracer
다양한 계정 활동 로그를 수집<br>
약 155종류의 네이버 클라우드 플랫폼의 액션로그를 수집한다.<br>
Management 콘솔, API, SDK, CLI를 통한 계정 별 액션 로그와 비 계정 활동에 대한 로깅 기능 제공<br>
Cloud Log Analytics와의 연동으로 로그 분석 및 로그를 엑셀로 다운로드 받거나 Object Storage로 Export 가능<br>

## Resource Manager
리소스들을 통합적으로 관리 서비스<br>
네이버클라우드플랫폼 서비스 내 생성한 모든 리소스를 한 눈에 볼 수 있는 통합 관리 서비스이다.<br>
목적에 따라 자원들을 그룹화하거나 태그를 지정하여 다양하게 활용가능하다.<br>
리소스 별 생성 및 변경 이력을 확인가능하다.<br>

## Data Analytics Service
웹 사이트 데이터 분석 서비스<br>
웹 사이트에 유입되는 방문자와 관련된 다양한 고객 행동 데이터 분석 환경을 제공<br>
Hadoop, Search 등 다양한 데이터 관리 및 분석을 위한 상품과 함께 이용가능<br>

## Effective Log Search & Analytics(ELSA)
ELSA의 SDK/API를 이용하여 어플리케이션을 쉽게 저장하고 검색,분석할 수 있는 로그 분석툴<br>
특정 로그 발생시 알람을 보내는 이벤트 기능과 App Crash Report도 제공 예정<br>

## Cloud Log Analytics(CLA)
시스템 로그 수집 분석 플랫폼<br>
Agent 기반으로 동작하고 Syslog,Apache log, MySQL Log, Tomcatt Log, Windows Event Log, MS-SQL error log 수집<br>
커스텀로그 기능을 통해 직접 로그 대상 지정이 가능하다.<br>
Object Storage와 연계가능하고 로그 파일 보관 기능을 제공한다.<br>

## Real User Analytics(RUA)
웹페이지 접속자 분석도구<br>
구글 애널리틱스와 유사한 상품으로 웹페이지 접속자에 대한 분석 및 통계 서비스<br>

## Cloud  Hadoop
하둡 클러스터를 보다 쉽고 편리하게 생성 및 관리한다.<br>
Apache Ambari를 기본으로 제공하여 하둡 클러스터의 관리 및 모니터링을 효율적으로 가능하다.<br>

## Cloud Search
사용자의 웹사이트에 검색기능제공<br>
다양한 인덱싱 구성 옵션제공, 다국어 및 불용어, 동의어처리기능 제공<br>
네이버 형태소 분석 처리기를 기반으로 한국어 처리<br>

## Elasticsearch Service
ElasticSearch 클러스터를 손쉽게 배포, 보호, 운영 및 확장하여 로그 분석, 검색 app 모니터링등을 수행할수있도록 제공하는 완전 관리형 서비스<br>
Elasticsearch Service 클러스터는 1대의 매니저 노드와 3대 이상의 데이터 노드로 구성<br>
Elasticsearch Service는 데이터 분석 및 시각화 플랫폼인 Kibana와 연계되어 데이터를 빠르고 정확하게 분석<br>

## Cloud Data Streaming Service
Apache Kafka Cluster를 쉽고 간편하게 구축<br>
링크드인에서 개발된 분산 메세지 시스템으로 다양한 데이터 혹은 API 호출을 처리하는 메세지 시스템<br>
기존 메시징 시스템 대비 단순하면서 뛰어난 TPS를 나타냄<br>
매니저노드 1대, Broker 노드 최소 3대로 시작<br>
VPC 내부의 구성<br>
클러스터 관리는 CMAK을 통해 관리<br>
