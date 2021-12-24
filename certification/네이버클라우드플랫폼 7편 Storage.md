---
title:  "네이버클라우드플랫폼 Storage"
excerpt: "네이버클라우드플랫폼 파헤치기 7편 "
toc: true
toc_sticky: true

categories:
  - cloud
tags:
  - 네이버클라우드플랫폼
  
last_modified_at: 2021-03-01T08:07:00-08:00
---

## Object Storage
__인터넷상에 원하는 데이터를 저장하고 사용할 수 있도록 구축된 오브젝트 스토리지<br>__
객체 기반의 무제한 파일 저장스토리지이다.<br>
콘솔,Restful API, SDK등의 다양한 방법으로 오브젝트들을 관리하고 저장된 파일은 각 파일마다 고유한 접근 URL 부여<br>
정적 웹사이트 호스팅 가능<br>
CDN,Transcoder,Image Optimizer, Cloud Hadoop, Cloud Log Analytics와 같은 NCP내 다양한 상춤과 통합<br><br>

## Archive Storage
데이터 아카이빙 및 장기 백업에 최적화된 스토리지 서비스<br>
Infrequent Data 백업 및 Archiving Data 보관을 주 목적으로하는 스토리지<br>
Object Storage보다 데이터 저장 비용은 저렴, 데이터 처리 API 비용은 비쌈<br><br>
콘솔,API,CLI,SDK를 이용해서 데이터를 관리할수있다.<br>
데이터 최소 보관 기간없이 사용할 수 있다.<br>
오브젝트 생명주기 관리가 가능하다.<br>
Sub Account 연동을 통한 권한 관리가 기능을 제공한다.<br><br>

## NAS
다수의 서버에서 공유하여 사용할 수 있는 스토리지<br>
최소 500GB에서 10TB까지 구성이 가능하다.<br>
NAS 가용량안에서 생성된 스냅샷 이미지 이용해서 데이터에 대한 복구 기능제공<br>
프로토콜은 NFS/CIFS를 제공한다.<br>
서버 사설IP를 이용하여 ACL오픈으로 타 계정 서버에도 마운트가능<br>

## Data Teleporter
대용량 데이터 이전을 위한 효과적인 솔루션<br>
대용량 데이터 이전을 위한 전용 어플라이언스 대여 서비스이다.<br>
네트워크 비용이 절검되고 안전하고 빠른 데이터 이관이 가능하다.<br>
이관 데이터를 NCP 오브젝트 스토리지 혹은 NAS에 Import가능하다.<br>

## Backup
서버 내 파일 및 preinstall DB에 대한 백업 설정<br>
백업 요청서를 작성하여 신청하고 서버에 Agent를 설치하면 끝나게된다.<br>
백업수행주기로는 다양한 옵션을 제공한다.<br>
최대 24주까지 백업파일이 보관가능하다.<br>

