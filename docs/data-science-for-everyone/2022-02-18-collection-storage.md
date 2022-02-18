---
layout: post
title:  "데이터 수집 및 저장"
parent: Data Science
nav_order: 2
date:   2022-02-18 20:48:00 +0900
---
# Data Collection and Storage
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 데이터 소스
---
### 회사 데이터
회사에서 수집된 데이터로 데이터 기반 의사결정을 할 수 있도록 활용
- 웹 데이터, 설문조사, 소비자, 물류, 금융 거래 데이터 등
- Net Promoter Score (NPS)

### 오픈 데이터
무료의 개방된 데이터로 누구나 사용 및 공유가 가능
- 데이터 API (Application Programming Interface)
    - 인터넷을 통해 데이터를 요청할 수 있음
    - 트위터, 위키피디아, 야후 파이낸스, 구글 맵 등
- 공공 기록: 국제 기구, 국내 통계청, 정부 기관

## 데이터 타입
---
데이터 타입에 따라 데이터를 저장하거나 분석 및 시각화하는 방식이 다를 수 있다.
- 이미지: 픽셀
- 텍스트: 리뷰
- 공간 (geospatial): 도로, 건물, 식물 위치 등
- 네트워크 등: 사용자 계정 간 팔로우 관계

### 양적 데이터 (Quantitative)
숫자로 측정되는 것
- 냉장고는 `60 inch`의 높이를 갖고, 내부에는 `2개`의 사과가 있고, 가격은 `1000불`이다.

### 질적 데이터 (Qualitative)
설명이 필요하며, 관찰될 수 있으나 측정되지는 않는 것
- 냉장고는 `빨간색`이고, `이태리에서 생산`되었고, 내부에서는 `생선 냄새`가 난다.

## 데이터 저장 및 검색
---
- 위치
    1. `On-premises cluster`: 자체 서버
    2. `Cloud`: Azure, AWS, Google Cloud
- 데이터 타입
    - 비구조적 형태 (이메일, 텍스트, 비디오/오디오, 웹 페이지, 소셜미디어) - `Document DB`
    - 테이블 형태 (Tabular) - `Relational DB`
- 검색

||쿼리 언어|데이터 타입|
|---|---|---|
|Document DB|NoSQL|Unstructured|
|Relational DB|SQL|Tabular|

## 데이터 파이프라인
---
다양한 데이터 소스 (공공 기록, APIs, DBs)와 서로 다른 데이터 타입 (비구조적, 테이블, 실시간 스트림 데이터)을 갖는 데이터를 처리
- 데이터를 정의된 단계로 전송하며, 데이터 수집 및 저장을 자동화함
- 빅데이터 프로젝트에 필수적이며, 데이터 엔지니어의 역할
- `ETL`: Extract - Transform - Load

Case Study: 스마트 홈

|데이터|소스|주기|
|---|---|---|
|날씨|기상청 API|30분|
|트윗|트위터 API|실시간 스트림|
|실내 온도|스마트 홈 온도계|5분|
|전등 상태|스마트 전구|1분|
|현관문 상태|스마트 도어|15초|
|에너지 소비|스마트 측정기|매주|

1. Extract: 모든 데이터를 데이터 소스로부터 가져옴
2. Transform: 서로 다른 데이터를 어떻게 사용하기 쉽게 조직화할 것인가?
    - 데이터 소스를 JOIN하여 하나의 데이터셋으로
    - 데이터 구조를 DB 스키마에 맞도록 변환
    - 관련없는 데이터 삭제
    - **데이터 준비, 관찰은 아직 수행되지 않음**
3. Load
4. Automation (ETL의 자동화)

