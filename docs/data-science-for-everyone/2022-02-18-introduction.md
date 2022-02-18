---
layout: post
title:  "데이터 사이언스란"
parent: Data Science
nav_order: 1
date:   2022-02-18 20:15:00 +0900
---
# Introdution to Data Science
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 데이터 사이언스란
---
저장된 대용량의 데이터 (예 - 좋아요 수, 클릭, 이메일, 카드 결제 기록, 트윗)로부터 현재 상태를 나타내거나 미래를 예측하는 (의미있는 정보를 만드는) 것

데이터로 할 수 있는 것
- 조직 또는 프로세스의 현재 상태를 나타낸다
- 비정상적 (anomalous) 이벤트를 감지한다
- 이벤트나 행동의 원인을 진단한다
- 미래의 이벤트를 예측한다

## 워크플로우
1. 데이터 수집 및 저장 (Data Collection & Storage)
2. 데이터 준비 (Data Preparation)
    - ~~different data type, missing values~~, ...
3. 관찰 및 시각화 (Exploration & Visualization)
4. 실험 및 예측 (Experiment & Prediction)

## 적용 분야
---
### 머신러닝 (Traditional Machine Learning, ML)
Case study: 위조된 거래 감지 (fraud detection)
- 다음과 같이 거래 기록 데이터가 주어졌을 때, 각 기록이 정상 거래인지 위조거래인지 구분

|Amount|Date|Location|...|
|---|---|---|---|
|149.62|2019-05-23|London|...|
|2.69|2018-10-03|Birmingham|...|
|378.66|2019-06-15|Liverpool|...|
|...|...|...|...|

ML을 수행하기 위해 필요한 조건
1. 잘 정의된 문제: 해당 거래가 위조되었을 확률은?
2. Example data: `위조` 혹은 `정상` 거래 기록들
3. 알고리즘에 적용할 새로운 데이터셋: 새로운 신용카드 결제 기록들

### 사물인터넷 (Internet of Things, IoT)
Case study: 스마트 워치
- 스마트 워치의 3축 가속도계 (accelerometer) 데이터가 주어졌을 때 해당 시계열 데이터를 보고 사용자의 행동 (예 - 달리기, 걷기, 앉기 등)을 인지

일반적인 컴퓨터가 아닌 가젯 (gadget)을 활용
- 스마트 워치
- 홈 보안 시스템
- 하이패스 (Electronic toll collection)
- 건물 에너지 관리 시스템

### 딥러닝 (Deep Learning, DL)
Case study: 이미지 인지 (image recognition)
- 여러 뉴런 (neuron)으로 구성된 학습 모델
- 대용량의 학습 데이터를 필요로 함
- 복잡한 문제 해결에 사용됨: 이미지 분류, 언어 학습/이해

## 역할 및 도구
---
### Data Engineer
정보를 설계하며, 데이터에 대한 접근을 관리하며 데이터 파이프라인 및 저장 솔루션을 구축한다 - `데이터 수집 및 저장`
- `SQL`: 데이터 저장 및 조직화에 필요
- `Java/Scala/Python`: 데이터 처리를 위한 프로그래밍 언어
- `Shell`: 태스크를 실행 및 자동화
- `Cloud Computing`: AWS, Azure, Google Cloud Platform

### Data Analyst
분석을 위한 데이터 전처리와 함께 데이터를 나타내는 간단한 분석 (데이터 요약 보고서나 대시보드)을 수행 - `데이터 준비, 관찰 및 시각화`
- `SQL`: 데이터를 검색하고 집계 (aggregate)
- `Python/R`: 데이터 전처리 및 분석
- `Spreadsheets - Excel, Google sheets`: 간단 분석
- `BI tools - Tableau, Power BI, Looker`: 대시보드 및 시각화

### Data Scientist
머신러닝 등 통계 방법론을 잘 다루며, 실험 및 분석을 통해 인사이트를 얻는다 - `데이터 준비, 관찰 및 시각화, 실험 및 예측`
- `SQL`: 데이터를 검색하고 집계
- `Python/R`: `pandas`나 `tidyverse` 같은 데이터 사이언스를 위한 라이브러리를 활용

### Machine Learning Scientist
딥러닝 기반 태스크 (이미지 처리, 자연 언어 처리 등)를 통해 데이터를 통한 예측 및 추정 - `실험 및 예측`에 심화
- `Python/R`: `Tensorflow`나 `Spark` 등의 머신러닝 라이브러리 활용

##