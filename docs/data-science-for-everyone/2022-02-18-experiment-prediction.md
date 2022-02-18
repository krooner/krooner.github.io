---
layout: post
title:  "실험과 예측"
parent: Data Science
nav_order: 5
date:   2022-02-18 21:54:00 +0900
---
# Experimentation and Prediction
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 실험 (Experiment)
---
실험은 의사결정을 유도하고 결론을 이끌어낸다.
1. 문제, 질문을 정의한다
2. 가설을 세운다
3. 데이터를 수집한다
4. 가설에 대해 통계적 검증을 수행한다
5. 결과를 해석한다

용어 정리
- 샘플 크기: 사용된 데이터 포인트의 수
- 통계적 유의성: `결과가 우연에 의한 것이 아니다`
    - 통계적 모델에 대해 가정을 세운다
    - 통계적 검정을 수행한다: `t-test, Z-test, ANOVA, Chi-square test`

Case study: 어떤 블로그 제목이 더 나은가?
- 문제 정의: `제목 A 또는 B 중 더 많은 클릭 수를 유발한 것은?`
- 가설 설정: `제목 A와 B는 동일한 클릭 수를 유발한다.`
- 데이터 수집:
    - 사용자 중 절반은 제목 A를, 나머지 절반은 제목 B를 본다
    - 목표한 샘플 크기에 도달할 때까지 클릭 비율 (click-through rate)을 추적한다
- 가설에 대한 통계 검증 수행:
    - `제목별 클릭 비율의 차이는 유의미한가?`
- 결과 해석:
    - 두 제목 중 하나를 선택하거나, 추가 실험을 하거나, 다른 실험을 설게한다.

### A/B Testing
Champion/Challenger Testing라고도 한다.
1. tracking할 metric을 결정한다: `click-through rate`
    - 전체 사용자 중 제목 링크를 선택한 사용자의 비율
    - 변화를 측정하기 위한 `baseline metric`을 구한다: 평소에 사람들이 얼마나 자주 블로그 제목을 클릭하는지
2. 샘플 크기를 계산한다.
    - `click-through rate`이 50%보다 훨씬 크거나 작은 경우, 샘플 크기를 키운다
        - 일반적으로 클릭 비율은 매우 낮다 ($<3\%$)
    - 샘플 크기가 클수록 작은 변화를 감지할 수 있다
        - (작은 샘플 크기) low sensitivity, large differences
        - (큰 샘플 크기) high sensitivity, small differences
3. 실험을 수행한다.
4. 유의성을 확인한다.
    - 만약 결과가 유의미하지 않다면?
        - difference는 우리가 선택한 임계값보다 작다
        - 검정을 더 오래하는 것이 도움이 되진 않는다

### 모델링
통계적 모델이란
- 통계로 실제 프로세스를 표현
- 임의변수를 포함하여 변수 간의 수학적 관계를 나타냄
- 통계적 가정과 이전 데이터를 기반으로 함

예측적 모델링 (Predictive modeling) <br>
`New Input` $\rightarrow$ `Predictive Model` $\rightarrow$ `Outcome`
- New Input (미래 특정 날짜, 트윗)
- Predictive Model (선형 회귀 방정식, Neural Net)
- Outcome (실업률, 가짜 트윗일 확률)

## 시계열 예측 (Time Series Forecasting)
---
시간에 따라 순차적으로 발생하는 데이터인 시계열 데이터 (주식 및 가스 가격, 실업률, 맥박 등)를 다루며, 과거 데이터로부터 예측 결과를 도출하는 모델을 만듦
- 다음 달 강우량?
- 30분 이후의 교통량 변화?
- 앞으로 6시간 동안의 주식 가격 변화?
- 20년 후의 인구 변화?

시계열 데이터

|Date|Rate|
|---|---|
|1976-01-01|7.1|
|1976-02-01|7|
|...|...|
|1991-01-01|10.3|
|...|...|
|2015-04-01|6.8|
|2015-05-01|6.8|

### 계절성 (Seasonality)
일정 주기마다 반복되는 특징
- 아이스크림 판매량이 여름에는 높고 겨울에는 낮다
- 소비량이 매월 말에는 높게 나타난다 (월급 들어오는 날)

![data_2](../../../assets/images/2022-02-18-image-2.png)

### 신뢰구간 (Confidence Intervals)
실제 값이 해당 구간 내에 발생할 것이라고 모델은 $x\%$ 확신함

![data_3](../../../assets/images/2022-02-18-image-3.png)

## 지도 기계학습 (Supervised ML)
---
`label`과 `features`를 갖는 데이터를 이용하여 `label`을 예측
- `label`: 예측하고자 하는 결과
- `features`: `label` 예측에 필요한 데이터
- 추천 시스템, 생의학 이미지 진단, 숫자 인식, 가입자 이탈률 (customer churn) 예측

Case study: 가입자 이탈률 예측
1. 학습 데이터로 예측 모델을 학습시킨다.
2. 새로운 소비자 데이터의 `features`를 예측 모델에 넣어 `label`을 예측한다.

### 학습 데이터 (Training data)
- `label`: 가입자 구독/해지 여부
- `features`: 소비자 데이터
    - 나이, 성별, 직업, 거주지, 최근 방문일 등

### 모델 평가 (Model evaluation)
이전 데이터를 학습 데이터와 테스트 데이터로 분할한다.

![data_4](../../../assets/images/2022-02-18-image-4.png)

## 비지도 기계학습 (Unsupervised ML)
---
`features`만 갖는 데이터 (`unlabeled data`)를 이용

### 클러스터링 (Clustering)
데이터를 여러 카테고리로 분류: 소비자 분할, 이미지 분할, 이상 감지 등에 활용됨

Case study: 새로운 품종 분류하기
1. `feature` 정의하기
    - 꽃 색깔, 꽃잎의 길이/너비, 꽃받침의 길이/너비, 꽃잎 수
2. `cluster number` 정하기
    - number에 따른 클러스터링 결과를 보고 직접 결정
    - domain knowledge가 최적의 수를 정하는데 필요할 수 있다
3. 문제 해결을 위해 `clustering result`를 활용

