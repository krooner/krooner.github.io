---
layout: post
title:  "Cloud Computing"
parent: 'DataCamp'
grand_parent: 'School (2013-2022)'
date:   2022-02-24 13:55:00 +0900
last_modified_date: 2024-06-18
---
# 클라우드 컴퓨팅이란
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

인터넷을 통해 사용한 만큼 (pay-as-you-go) 비용을 부과하는 기술 서비스들을 제공하는 것
- 데이터 분석 또는 AI 모델 적용을 위한 연산
- 데이터 백업 또는 복구를 위한 저장, 데이터베이스 
- 음성 데이터나 비디오 데이터 스트림을 수신/발신하는 네트워크
- 클라우드 기반 어플리케이션 등 소프트웨어

> 웹사이트 호스팅을 하려고 할 때
> 1. DataCamp의 무료 프로모션 동안 사용자 수가 급증한다
> 2. 트래픽이 증가하여 서비스 속도가 느려진다
> 3. 사용자들은 서비스 품질 저하를 체감하고 떠난다

|온프레미스 On-premise|클라우드 Cloud|
|---|---|
|서버를 직접 설치한다. 사용자가 증가할수록 새로운 서버를 구매 또는 임대해야한다. 설치에 시간적, 경제적 비용이 든다.|필요할 때 즉시 컴퓨팅 파워를 활용할 수 있다. 사용자가 증가하면 더 많은 클라우드 서버에 접근한다.|

## 클라우드 컴퓨팅 특성

|특징|설명|
|---|---|
|가상화|클라우드 컴퓨팅에 있어 토대가 되는 기술. 물리적 서버를 여러 개의 가상 서버로 활용 (규모의 경제) 하며 개별 서버의 성능을 최대화한다|
|확장성|필요한만큼 리소스를 쉽게 제거 및 추가하는 scale-up. `Vertical Scaling`의 경우 인스턴스의 파워를 향상시키며, `Horizontal Scaling`은 더 많은 인스턴스를 추가|
|비용|하드웨어나 소프트웨어 구매 비용이 없는 `Pay-as-you-go` |
|속도|클라우드 리소스에 사용가능할 때 즉시 접근할 수 있는 On-demand (요구사항에 따라 즉시 공급)|
|성능|컴퓨팅 리소스에 빠르고 효율적인 접근이 가능한 `Data center` (조직의 IT 작업이나 장비를 설치)|
|성장|넓은 범위의 리소스와 서비스를 활용함|
|신뢰성|데이터 및 서비스의 보장된 내구성과 이용가능성을 제공. 데이터는 데이터 센터를 따라 복제되어 있다. 자연재해가 발생해도 이용가능성을 보장됨.|
|보안|데이터의 안전한 저장 및 관리|

## 클라우드 서비스 모델

||IaaS|PaaS|SaaS|
|---|---|---|---|
|의미|Infrastructure as a Service|Platform as a Service|Software as a Service|
|추상화|LOW|MID|HIGH|
|제어|HIGH|MID|LOW|
|정의|온프레미스 인프라를 클라우드 기반으로 대체|앱 개발에 사용되는 HW & SW 툴|(월 구독료 지불로 사용가능한) SW|
|장점|고비용의 온프레미스를 대체하여 확장가능성 추가|앱 개발할 때 필요한 초기 과정을 생략|컴퓨터에 SW 설치할 필요 없음|
|사용자|시스템 관리자|개발자|사용자|
|예|클라우드 서버 (AWS, Azure, Google Compute Engine)|웹/로직 앱 (Google App Engine, Microsoft Azure, AWS Elastic Beanstalk)|인터넷 앱 (Google G Suite, MS Office 365, Dropbox)|

> 다른 클라우드 서비스 모델
> - FaaS (Function as a Service, SW의 일부인 function에 초점을 맞추며 개인 인증이나 지불 거래 등)
> - HaaS (Hardware - ), SaaS (Storage - ), ...

## 클라우드 배치 모델

|특징|설명|
|---|---|
|Private cloud|클라우드 인프라를 사용자가 독점적으로 사용하며, 네트워크 링크를 통해 접근 가능. 리소스 및 데이터를 직접적으로 제어하는 장점이 있으나 사전 투자비용이 높음. On-demand 연산 리소스를 위한 가상화를 활용함.|
|Public cloud|클라우드 인프라는 공유되고 일반 사용자가 사용가능하며, 클라우드 서비스 제공자에 의해 소유되고 관리된다. 최소 투자로도 빠르게 시작가능하고 확장하기 쉬우나, 데이터 센터나 하드웨어에 접근할 수 없다.|
|Hybrid cloud|두 개 이상의 다른 클라우드 모델을 혼합한다. 데이터 분석을 위해 민감한 데이터는 Private cloud에, 앱은 Public cloud에서 실행. `Cloud bursting` - Private cloud의 capacity가 꽉 찼을 때, 서비스 중단을 막기 위해 임시적으로 Public cloud를 활용함|
|Multi-cloud|다른 클라우드 제공자의 서비스들을 결합. 가격 정책과 서비스 제공에 있어 유연하고 특정 사용자에 의존할 필요가 없다|
|Community|특정 커뮤니티의 독점적 사용을 위한 인프라로, 내부 또는 외부적으로 관리되고 호스팅됨|

## 클라우드 규제
개인 데이터란 살아있는 개인 (living individual)을 식별할 수 있는 정보로, 수집되어 특정 사람을 식별할 수 있는 경우에는 부분적 정보라도 개인 데이터로 간주된다. 집 주소, 이름, 이메일 주소, 위치, IP 주소 등 Personally Identifiable Information (PII)

> 일반 데이터 보호 규제 (GDPR) 의 경우
> - EU 내 사용자의 개인 데이터를 어떻게 수집, 처리, 저장할지를 규제
> - 사용자는 데이터 수집을 explicit하게 동의해야 함
> - 정보는 암호화되고 익명화되어야 함
> - 동일한 수준의 데이터 보호를 보장할 수 없는 경우 개인 데이터는 EU 밖으로 유출될 수 없다

## 클라우드 역할

|역할|설명|
|---|---|
|Data Scientist|클라우드에서 연산적으로 고비용의 분석을 수행|
|ML Engineer|클라우드에서 ML 모델을 학습 및 배치|
|Data Engineer|빅데이터를 수집, 변환, 저장하기 위한 파이프라인을 클라우드에 구축|
|Data Analyst|BI 툴을 통해 클라우드 내 데이터에 접근|
|Cloud Architect|주어진 비즈니스 문제에 대한 클라우드 인프라를 설계하고 인프라 배치를 계획. 최적 비용과 규모확장성을 보장|
|Cloud Engineer|클라우드 서비스를 개발, 유지 및 모니터링하며 클라우드에 작업을 이식 (migrate)|
|DevOps Engineer|SW 개발과 IT 작업의 결합. Infrastructure as code (IaC) 와 같이 소프트웨어 개발과 자동화를 통해 클라우드의 신뢰성, 이용가능성, 규모확장성을 보장|
|Security Engineer|보안 요구사항을 명시하며 클라우드 내 데이터의 보안을 테스트 및 검증. 조직과 사용자의 데이터 보호에 책임|