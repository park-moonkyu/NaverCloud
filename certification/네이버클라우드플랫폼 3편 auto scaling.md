---
title:  "네이버클라우드플랫폼 오토스케일링(Auto Scaling)"
excerpt: "네이버클라우드플랫폼 파헤치기 3편 "
toc: true
toc_sticky: true

categories:
  - cloud
tags:
  - 네이버클라우드플랫폼
  
last_modified_at: 2021-02-13T08:07:00-08:00
---

##  오토스케일링
클라우드의 장점중 하나는 유연한 인프라 확장이다.<br>
유연한 인프라 확장은 곧 비용을 최적화를 의미하기도 한다.<br>
이러한 유연한 인프라는 사용자가 정의한 스케줄, 사용자가 설정한 모니터링, 요청에 따라 서버가 동작한다.<br>

### Launch Configuration
오토스케일링시에 필요한 설정으로 이름으로 구분되고 한 계정 내에 유일하다.<br>
액션의 대상이 되는 서버의 기본 템플릿(이미지,서버 타입, ACG 등)<br>
베이스 이미지는 퍼블릭이미지이고 커스텀 이미지인 내 서버 이미지에 사용이 가능하다.<br>

### AutoScaling Server Group
Scaling, Management, 액션을 위한 논리적인 그룹이다.<br>
miniSize <= desiredCapacity <= maxSize 대소 관계 유지<br>
<br>

### 프로세스
개발자는 API 또는 콘솔UI로 직접 설정을 한다. 그럼 어떻게 설정하는지 하나씩 적어보자.<br>
우선 Launch Configuration을 설정한다. 서버원본이미지를 선태하고, 서버, 이름, 인증키를 설정한다.<br>
그후, Auto Scaling Group을 설정한다.<br>
그런다음 스케줄링 기반 Auto Scaling, 서버 그룹 모니터링 기반 AutoScaling을 설정한다.<br>
이렇게 설정이 끝나면 설정한 이벤트 조건에 맞춰 용량조정(Scaling)을 수행하게되는것이다.<br>
<br>
예를들어 모니터링기반의 오토스케일링을 설정했다고 하면 CPU 사용량이 50% 이상이 5분넘게 지속되면 서버 2대를 늘린다.<br>
혹은 오후6~8시까지는 주문량이 늘기때문에 해당시간에 가상서버를 자동 증설하자!<br>
<br>

## 용어 정리
Scale in / Scale Out : 오토스케일링 그룹을 생성하여 고객이 설정한 정책에 따라 사용하고 있늩 가상 서버의 자동확장 및 자동 축소 제공<br>
Auto Scaling Group : 여러 개의 서버 인스턴스들을 Auto Scaling Group이라는 하나의 그룹으로 묶어 놓기.<br>
Launch Configuration: Auto Scaling Group에서 가상 서버를 시작 구성하는데 사용하는 템플릿. 즉, 오토스케일링 그룹을 생성할때에는 Launch Configuration을 지정해야한다.<br>
최소/최대 용량 : Auto Scaling Group의 최소/최대 서버 수. 최소보다 항상 이값과 같거나 이같보다 더 큰 서버수가 유지. 서버를 한 대도 보유하지 않을 수 있게 하려면 0으로 설정.<br>
기대용량 : 서버의 수는 기대 용량값에 따라서 조정된다. 이 값은 최소용량 이상, 최대용량 이하.<br>
쿨다운기본값 : 쿨다운시간이랑 실제 스케일링이 수행 중이거나 수행 완료된 이후에 모니터링 이벤트 알람이 발생하더라도 무시하도록 설정한 기간.<br>
헬스체크 : Auto Scaling Group의 가상 서버에 주기적인 상태확인을 수항하여 상태가 비정상인 가상 서버를 식별<br>

