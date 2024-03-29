---
layout: post
title:  "HAR with SEP and Clustering"
date:   2021-05-08 16:00:00 +0900
parent: Research Topic
grand_parent: School
nav_order: 5
---
# 행동 분할 및 클러스터링을 적용한 행동 인지 모델
{: .no_toc }

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

## 논문
---
D. Chen, S. Yongchareon, E. M. -K. Lai, J. Yu and Q. Z. Sheng, ["Hybrid Fuzzy C-means CPD-based Segmentation for Improving Sensor-based Multi-resident Activity Recognition,"] in IEEE Internet of Things Journal, doi: 10.1109/JIOT.2021.3051574.

["Hybrid Fuzzy C-means CPD-based Segmentation for Improving Sensor-based Multi-resident Activity Recognition,"]: https://ieeexplore.ieee.org/document/9324819


## 문제 정의
---
**Improving Multi-resident** Activity Recognition performance

## 문제가 중요한 이유
---
`Multi-resident Activity Recognition, HAR`
* Single-resident 환경에 대한 연구는 많았으나, **Multi-resident에서의 연구는 초기 단계**
  - 실제 환경은 Multi-resident인 경우가 많기 때문에 연구가 필요함

`Activity Segmentation`: Recognition을 향상시키는데 **Segmentation**이 중요함
  - Single-resident 환경에서는 Sliding window 방식으로 sensor stream을 분할함
  - **그러나 Multi-resident에서는 기존 방식으로 Activity boundary를 파악하기 어려움**
    - 기존 Activity Segmentation은 대부분 **pre-segmented data**를 필요: real-time application에 적용할 수 없는 **offline** 방식
    - 많은 사용자가 공간에 있으므로 **매우 Complex한 Activity를 보임**
      1. Parallel Activity: 여러 명이 각자 일을 동시에 수행
      2. Collaborative Activity: 여러 명이 동일한 일을 함께 수행

  - **Complex Activity를 잘 Recognize하려면 Segmentation을 제대로 하는 것이 필요함**: 각 Segment가 Single-resident의 ongoing activity를 나타내도록 분할

## 문제 해결을 위한 기존 방식
---
`Data-driven segmentation`
- **Sliding window**: 
  - time-based (continuous and periodic event에 적절함)
  - event-based (discrete event에 적절함)
  - **Limitation: Finding Optimal Size**
- **Dynamic approach**:
  - Sensor correlation: Pearson product-moment correlation (PMC)
  - Time correlation: different action timeframe이 동일한 time division에 속하는지
- **Change Point Detection (CPD)**:
  - **SEP**: 확률분포비율을 추정, dissimilarity measure로 Separation distance를 사용함

`Knowledge-driven segmentation`
  - KCAR (Knowledge-driven Concurrent Activity Recognition)
    - Semantic 추출 > Semantic간 Similarity 계산 > Pyramid Match Kernel로 Activity Identification
  - Semantic-based: generic knowledge와 resident-specific preference를 활용함
  - Statistical learning + Ontology:
    - (Offline) clustering and ontology update
    - (Online) determining optimal size and using SVM

`Multi-resident recognition model`
* naive Bayes: multi-residents의 location tracking
  - Limitation: temporal process modeling에 부적합함
    - Deep Belief Network이 더 적합할 수 있음
* Hidden Markov Model (HMM): CL-HMM > Parallel HMM, Coupled HMM
* LSTM and GRU: LSTM < GRU
    - LSTM (too many parameters: computational complexity)
    - Data association problem


## 제안 방법론
---
Multi-resident AR: Activity boundary를 알기 위해서는 먼저 어떤 resident가 event *t*를 trigger했는지 알아야 함
- Sensor location에 대한 Clustering을 활용해서 sensor event를 trigger한 user를 알아낸다
- 각 user의 subsequence에 대해 CPD 알고리즘을 적용하여 각 사용자들이 행동을 전환하는 지점을 찾는다

1. `Data collection`
2. `Clustering (Fuzzy C-Means, FCM)`
  - FCM: Fuzzy Theory를 기반으로 하는 objective function의 optimization
    - Clustering 결과: 각 cluster center에 대한 membership degree (weight) matrix 
    - 각 Sensor의 location 값을 기반으로 divide stream into *N* clusters
    - Assumption: collaborative activity는 같은 장소, parallel activity는 다른 장소에서 수행된다.
3. `SEP algorithm` to each clustered subsequence
    - detect the amount of change from **first sensor sequence** to **next sensor sequence**
    - a sequence of events between two change events = segment
4. `Use a set of segments for recognition`
  - Traditional and SOTA models
  - Comparison with other results using different segmentation methods
    - sliding window (event-based and time-based)
    - dynamic segmentation


## 결과
---
CASAS에서 제공하는 [adlmr] (Activities of Daily Living of multi-resident) dataset 등 two-resident의 행동 데이터셋을 활용함

[adlmr]: http://casas.wsu.edu/datasets/adlmr.zip

Segmentation 비교를 위해 다음 방법론을 baseline으로 삼음
- Sliding window approach
- Correlation-based approach

Recognition 비교를 위해 다음 방법론들을 baseline으로 삼음
- Traditional ML approaches
- DL approaches (LSTM, GRU, ...)

Segmentation 성능에 대한 언급은 없고, Recognition 성능에서 `Proposed segmentation scheme + GRU` 모델에서의 HAR 성능이 가장 높게 나타남.

## 의견
---
Clustering 과정에서 `number of clusters` 즉, 현재 행동 데이터에 대해 행동에 참여 중인 사용자의 수를 미리 알고 있어야 한다.

두 명의 사용자들의 행동은 크게 `Individual activity`와 `Collaborative activity`로 분류할 수 있는데, `Collaborative activity`의 경우 사용자들이 서로 근접하여 행동하기 때문에 어떤 사용자에 의해 센서 이벤트가 만들어졌는지 알기가 어렵다. 즉, clustering의 성능이 `Collaborative activity`의 경우에는 떨어진다.

`SEP` 자체로도 Computation overhead가 높아서 실시간으로 변화 점수 결과를 얻을 수 없는데, `Fuzzy C-Means` 또한 센서 이벤트가 많아질수록 Computation이 점점 많아지기 때문에 실제 해당 방법론을 적용하여 실시간으로 들어오는 센서 데이터에 대한 결과를 얻기 어렵다.


