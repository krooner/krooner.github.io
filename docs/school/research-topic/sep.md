---
layout: post
title:  "SEP"
date:   2021-05-06 16:00:00 +0900
parent: Research Topic
grand_parent: School
nav_order: 3
---
# Separation Distance
{: .no_toc }

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

## 논문
---
_S. Aminikhanghahi, T. Wang and D. J. Cook, [**"Real-Time Change Point Detection with Application to Smart Home Time Series Data,"**] in IEEE Transactions on Knowledge and Data Engineering, vol. 31, no. 5, pp. 1010-1023, 1 May 2019, doi: 10.1109/TKDE.2018.2850347._

[**"Real-Time Change Point Detection with Application to Smart Home Time Series Data,"**]: https://ieeexplore.ieee.org/document/8395405

## 문제 정의
---
***(near) Real-time and Unsupervised*** Change Point Detection Algorithm을 제안함

## 문제가 중요한 이유
---
CPD를 `행동 분할`에 적용하기 위해서는 
* `Real-time`으로 센서 이벤트의 행동 전환점 여부를 판단해야 함
* Human activity는 dynamic하기 때문에 학습 데이터 (e.g. pre-segmented data) 없이도 행동 분할을 수행할 수 있어야 함

## 문제 해결을 위한 기존 연구
---
*Supervised* with labelled training data
  - `Multi-class classifier`
    - 많고 다양한 training data 필요: 각 Activity 에 해당하는 data + 모든 Transition data
  - `Binary classifier`
    - **가능한 Transition type이 많아질수록 학습의 Complexity가 급상승**
  - `Virtual Classifier (VC)`
    - two consecutive window pair에서 first window에는 +1, second window에는 -1 (hypothetical label)을 부여하여 decision tree같은 rule-based model로 학습시킴 (VC는 각 pair마다 존재)

*Unsupervised* with statistical feature of data
  - **모든 change cases에 대한 prior knowledge 학습 없이, 다양한 situation에 대응할 수 있음**
  - `Subspace Modeling`: data를 state space로 표현하고, change point를 state space 내 distance로 감지함
      - Subspace Identification (SI): 각 sliding-window에서 생성된 state space model에서 matrix를 생성한 후, subspace 간 gap을 계산
      - Singular Spectrum Transformation (SST): 두 windows 각각 trajectory matrix에서 singular spectrum을 비교
  - `Probabilistic Methods`: 이전 Change Point Candidate event에서부터 얻은 data와 새로운 window의 확률 분포를 추정
      - Bayesian CPD: 현재 event의 run-length **r** (elapsed time from prev CP candidate)를 추정, 다음 event의 **r'**: 0 (현재 event가 CP로 감지됨) 또는 **r+1** (otherwise)
      - Gaussian Process (GP): data를 noisy Gaussian distribution function value로 표현, predicted value와 actual value를 비교함
  - `Clustering Methods`: data를 클러스터링 한 다음, Cluster state feature의 difference를 계산
      - SWAB (Sliding Window and Bottom-up): 각 event를 separate sequence로 본 다음 merge해서 subsequence로 만듦 + buffer에 있는 change point data를 빼내고 다음 data를 넣음
      - MDL-based: bottom-up greedy search: cluster 수를 정의하지 않아도 됨
      - Shaplet-based: greedy search + time-series shape을 기반으로 클러스터링
  - `Kernel-based Methods`: data를 high-dimensional feature space에 맵핑하고, 각 feature의 homogeneity를 비교함
  - `Graph-based Methods`: data를 각 node로 하는 graph로 표현한 뒤 two-sample statistical test로 detection
  - `Likelihood-ratio Methods`
      - Density ratio CPD: 두 연속적인 windows의 확률 분포가 동일하다는 건 같은 state에 있다는 것
      - Cumulative Sum (CUSUM): input의 특정 target에 상대적인 deviation을 누적시키고, 누적 값이 threshold를 초과했을 때가 Change point.
      - Change Finder (CF): pre-defined parametric model을 사용하므로 less flexible
  - `Direct density-ratio estimation`: windows 각각에 대한 확률-밀도추정없이, 바로 확률밀도"비율"을 추정하는 non-parametric Gaussian Kernel model 
    - ***dissimilarity measure (dm)***: 두 windows 간 change point의 존재 여부를 결정하기 위한 difference measurement
      - **`KLIEP`**: KL-divergence (KLDiv)를 dm으로 두고 density ratio를 추정
      - **`uLSIF`**: Pearson-divergence (PEDiv) 를 dm으로 두고 추정
      - **`RuLSIF`**: uLSIF의 문제 (second window 분포에 따라 dm 값이 기하급수적으로 커질 수 있음) 개선을 위해, alpha-relative PEDiv를 사용
      
    
## 제안 방법론
---
Data 내 미세한 변화에도 sensitive한 Change Point Score를 적용하는 `Separation Distance Metric`을 사용함
  
행동 분할 과정
  1. `Data Collection`
  2. `Sliding event window` with 30 sensor events
  3. `Event feature extraction` each feature corresponds to each event
  4. `SEP` (n = 2 feature windows per sample)
  5. detect change points with `threshold = 0.1`

## 결과
---
Artificial Dataset에 대하여 전반적으로 **SEP > RuLSIF > uLSIF** 순으로 좋은 ATD Performance를 보임
    
CASAS의 Single-resident Smart Home 데이터를 활용하여 행동 분할 성능 평가
  - Motion and Door Sensor (Discrete Binary)
  - 6 apartment datasets
  - 12 Activities (11 pre-defined + "Other" Activity)
  - (True Positive Rate과 False Positive Rate 간 ROC-AUC Curve, Mean Absolute Error 모두) 역시 **SEP > RuLSIF > uLSIF**
      
Other Real-world Dataset: **SEP의 TPR도 높지만, FPR도 가장 높음**
  - FPR이 높다 = Wrong Detection이 많다 = Segmentation이 제대로 되기 어렵다
  
## 의견
---
논문에서 설명한 Improvement 또는 Limitation
- 이전 Window가 현재 이벤트의 Dissimilarity Score에 미치는 영향 (information)을 고려하면 개선할 수도 있을 것이다
- Threshold Selection이 Performance에 직접적으로 영향을 준다
- SEP의 Computational Cost가 너무 크다 - computational efficiency를 요한다
  - 2-real time 알고리즘이라고 말하긴 했지만, 사실 event 하나에 대해 SEP를 수행하는 것도 Replication 기준 1초 내외가 걸림
  - 수십-수백만 이벤트에 대해 SEP를 적용하면 Calculation Delay가 너무 커서 Real-time Application을 시도할 수 없음

Replication을 하면서 생긴 의문점
  - **Cross-validation은 Target Dissimilarity Measure를 최소로 하는 Parameter를 정함**.
   그러므로 기존 direct density-ratio based CPD (uLSIF) 와는 다른 objective function을 써야한다고 생각함
  - 근데 왜 이 논문은 그런 과정을 쏙 빼고, "Cross-validation으로 구하면 된다" 라고 하고 uLSIF cross-validation에 대한 Reference를 걸고 그냥 넘어가지?
   이렇게 보면 그냥 동일한 Loss function을 사용한 것으로 볼 수 밖에 없음. **과연 이렇게 해석하는 것이 맞는 것인가**
  - Separation distance도 **max(0, 0.5-k), k>0** 로 뒀으면서, 그래프를 보면 또 [0, 1] 을 Y값으로 한다.
  - 이 알고리즘을 활용한 Activity Segmentation 논문을 Baseline으로 삼고 Replication을 하고 있는데, 이런 점이 헷갈려서 저자에게 메일을 보냈는데 읽씹당했다.