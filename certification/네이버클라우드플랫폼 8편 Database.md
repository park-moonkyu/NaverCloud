---
title:  "네이버클라우드플랫폼 Database"
excerpt: "네이버클라우드플랫폼 파헤치기 8편 "
toc: true
toc_sticky: true

categories:
  - cloud
tags:
  - 네이버클라우드플랫폼
  
last_modified_at: 2021-03-06T08:07:00-08:00
---

## Cloud DB for MySQL
자동 Fail-over 지원 및 사용자 환경에 맞는 구성이 가능하다<br>
최대 32v CPU에 256GB 메모리를 지원하고 6TB 자동디스크 확장이 가능하다.<br>
자동 Fail-over를 지원하며 최대 5대까지 복제 Slave 확장이 가능하다.<br>
Private Load Balancer를 이용해서 Read 부하분산이 가능하다.<br>
자동 백업 주기를 설정할수있다 최대 30일 백업파일이 보관된다.<br><br>
### 특징
#### Master DB Failover
콘솔에서 수동으로 Fail-over 실행가능<br>
서비스 오픈전에 Master DB장애로 Failover가 발생하는 상황을 재현하여 Application에 영향이 없는지 사전에 점검가능.<br>

#### DB Process 모니터링
DB 서버를 연결하여 수행중인 Query를 확인할 수 있다.<br>
슬로우 쿼리 로그 외에도 특정 시점에 어떤 Query가 수행중인지 확인할 수 있어 DB상태를 점검하는 데 도움<br>
#### Stand Alone백업
Stand Alone서버도 DB백업을 사용할수있다.<br>
데이터가 삭제되어서 백업 보관일 설정 내에서 백업으로 데어트를 복구가능<br>
#### 멀티존 지원
Master DB 서버 2대를 서로 다른 Zone에 생성하여 높은 가용성 제공한다.<br>
Master DB 서버는 같은 속성의 Subnet에 위치시킨다.<br><br>
#### Public Subnet과 Private Subnet에 구성 차이
Public Subnet에 구성하는 경우 Public도메인 구성가능하나, Private Subnet은 구성이 불가하다.<br>
<br>
## Cloud DB for Redis
### Classic 환경
자동 복구를 통해 안정적으로 운영되는 완전 관리형 클라우드 인메모리 캐시 서비스<br>
Redis가 제공하지 않는 자동 Fail-over 기능 개발하여 제공<br>
설치 후 Redis와 OS모니터링을 이용가능하며 장애 또는 이벤트 발생시 SNS알림<br>
CPU는 기본 4core만 제공<br>
Redis Cluster는 지원하지 않는다.<br>
기본포트는 : TCP 6379<br>
### VPC 환경
Redis Cluster를 제공한다.<br>
VPC내 Private Subent에 구성한다.<br>
샤드는 최소 3개이다.<br>
Config Group을 통해 설정적용이 가능하다.<br>
HA구성을 지원한다.<br>
CPU는 기본 4core만 제공한다.<br>

## Cloud DB for MS-SQL
### Classic 환경
안정적인 서비스 제공을 위해 장애발생시 자동 Fail-over기능 제공<br>
설치 즉시 MSSQL,모니터링 이용할수있으며, MSSQL의 동작상황을 그래프를 통해 손쉽게 확인 가능하다.<br>
1분 단위의 쿼리 레벨 성능 분석을 지원하여 서비스 성능과 안정성을 향상시킨다.<br><br>

### VPC 환경
안정적으로 운영되며, 장애발생시 자동복구<br>
최신버전의 MSSQL 2019 Standard Edition 제공<br>
설치 즉시 MSSQL,모니터링 이용할수있으며, MSSQL의 동작상황을 그래프를 통해 손쉽게 확인 가능하다.<br>
1분 단위의 쿼리 레벨 성능 분석을 지원하여 서비스 성능과 안정성을 향상시킨다.<br><br>

