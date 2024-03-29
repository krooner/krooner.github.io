---
layout: post
title:  "HAR using SEP"
date:   2021-05-07 16:00:00 +0900
parent: Research Topic
grant_parent: School
nav_order: 4
---
# SEP를 적용하여 HAR 성능 향상시키기
{: .no_toc }

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

## 논문
---
Samaneh Aminikhanghahi, Diane J. Cook, [Enhancing activity recognition using CPD-based activity segmentation], Pervasive and Mobile Computing, Volume 53, 2019, Pages 75-89, ISSN 1574-1192, doi.org/10.1016/j.pmcj.2019.01.004.

[Enhancing activity recognition using CPD-based activity segmentation]: https://doi.org/10.1016/j.pmcj.2019.01.004

## 문제 정의
---
인간 행동 인지 `Human Activity Recognition (HAR)` 모델의 정확도를 향상시키기 위해서는 정확한 행동 분할이 필요하다: Real-time Activity Transition Detection (ATD)으로 얻은 Information (Feature)를 활용한다.

## 문제가 중요한 이유
---
Human Activity Learning은 다음과 같이 분류할 수 있음: `Activity Recognition`, `Detection`, `Segmentation`, `Forecasting`

*Activity Segmentation*:
  - **Activity의 Boundary**를 알면 Activity duration, start/end time 등 **Activity의 특징을 잘 반영하는 Feature**를 활용하여 **Recognition 성능을 개선할 수 있음**
  - **Transition-aware Activity Segmentation**을 제시함


## 문제 해결을 위한 기존 연구
---
**기존 Activity Segmentation**은 `Video` 또는 `Wearable data` (Accelrometer, gyroscope, ...) 활용: 이후 IoT의 등장으로 **Sensor-based stream segmentation** 문제가 새로 등장함

Previous Sensor Segmentation
  - **Threshold**를 기준으로 Static Activity에서 Movement Activity로의 변화 감지
  - Wavelet Decomposition Model, Crowd-sourcing, LSTM, Two-step Supervised Classifier (Neural Network and HMM), ...
  - **Limitation**
    - `Supervised with Scripted Environment`: 사용자들은 정해진 instruction에 따라서만 행동하며 data를 생성하므로 real-world 환경에서의 sensor data와는 차이가 있다.
    - Real-world에서의 stream은 다른 activity 간 `boundary를 정의하기 매우 어렵다`: Unsupervised approach가 필요하다

Unsupervised Approaches
  - `SVM + Association Rule Mining`:
    - SVM은 raw sensor events로 Activity Recognition을 하거나, boundary information을 찾음
    - ARM은 boundary recognition 결과를 확인함
  - `Probabilistic SVM`
  - **Three** different `Decision Trees`
    - Transition Activity `Detector`, `Non-transition` Activity Classifier, `Transition` Activity Classifier
  - `Multivariate Online Change-detection Algorithm (MOCA)`: based on statistical values (mean, variance-covariance matrix)
    - continuous-valued feature를 사용하며 Data는 Gaussian Distribution을 따름
  - `RuLSIF` (for ATD) and HMM (for Recognition)

**Activity Segmentation**은 Recognition에 benefit을 줄 수 있으나, 현재는 **manually segmented 또는 sliding window** 방식을 사용하고 있음
  - **Input length에 independent한 RNN Model**이 있지만 **Supervised approach with large amount of data**이므로 PASS
  - ATD에는 Supervised and (RuLSIF-based) Unsupervised classifier가 있는데,
    - Supervised; not appropriate in real-time (sufficient labelled data)
    - ***Unsupervised*** approach with (near) real-time = **SEP**
      - activity에 대한 prior knowledge 없이 **Feature space에서의 data distribution 변화로 transition을 감지** 


## 제안 방법론
---
Four approaches에 대한 experiments

`AR-W`: **traditional sliding-window** based AR
  - *No Change Point Information*

`AR-WT`: AR-W + **additional features** from latest detected transition
  - Feature 중에서 **Change Point 직후에 발생한 Sensor의 Occurrence에 더 많은 Weight을 추가**

`AR-SM`: AR-W + all event labels between two transitions are defined by the **majority activity label**
  - 새로운 Transition을 감지하면, 이전 Transition부터 지금까지의 모든 event를 통틀어 majority인 label을 두 Transitions 사이의 모든 Event에 부여함

`AR-SS`: **transition 사이의 event subsequence를 single activity로 정의함**
  - Event 단위로 보는 것이 아니라, Transition 사이의 segment 단위로 봄
  - 주요 Features에는 More relevant한 정보가 담길 것이다: Activity Duration, dominant sensor and location, ...  

Process of SEP
1. fixed-length **sliding window** (30 events)
2. extracted **features** from windows **(for ATD)**
    - `Time feature`: day of week, time of day (from latest event in window)
    - `View feature`: window duration, most frequent sensor, complexity (entropy-based), activity change
    - `Sensor feature`: occurrences of each sensor event in window, last time each sensor fired
3. **SEP** between **two consecutive change point views (*n* = 2)**
    - 여기서 말하는 Window 또는 View는 모두 **Segmentation** 단계에 해당됨: Recognition에 쓰일 Window와 무관함
    - 각 Event에 매겨진 Dissimilarity Score 중, **Threshold (=0.3)** 이상의 local peak value가 최종 Change point candidate
    - 2-real time algorithm: **현재 event t**가 Change Point인지 알기 위해서는 **event *t+1* and *t+2***가 필요하다.

`Activity Recognition`은 **Random Forest Classifier** with 100 decision trees

## 결과
---
**29**개의 CASAS Apartment Dataset을 사용함: **Single-resident, Discrete binary sensors (Motion and Door)**

실제 Transition Time 기준으로, **10초 내에 Change Point Candidate이 있으면 True Positive**

||SEP|RuLSIF|
|---|---|---|
|TPR|**0.88**|0.87|
|FPR|**0.12**|0.19|


|Confusion matrix|AR-W|AR-WT|AR-SM|AR-SS|
|---|---|---|---|---|
|Accuracy|0.633|0.671|0.506|**0.681**|
|F-measure|0.689|0.729|0.606|**0.735**|


AR-W과 AR-WT는 complete real-time이지만, **CPD를 적용하는 AR-SM과 AR-SS는 Processing Delay가 발생하므로 real-time이 아닐 수 있음**

`Normalized Edit Distance`: Predicted activity sequence가 Actual activity sequence와 얼마나 차이가 나는지 보여주는 지표
  - AR-W (1.0)과 AR-WT (1.1)보다, **CPD를 적용하는 AR-SM (0.4)과 AR-SS (0.3)이 더 낮은 값**을 보임

`Gini Importance Value`: AR-WT에서 Transition Feature를 추가한 것이 정말 효과가 있었는지 (Random Forest의 Structure를 변화시켰는지)
  - Current Sensor ID > **Transition Event Sensor ID > Weighted Sensor Occurrence** 순으로 Importance가 컸음
    

  
## 의견
---
논문에서 설명하는 Main Problem과 Limitation
  - `Noise`가 Recognition에 영향: Sensor or environmental noise, data collection, incorrect g.t. labelling
  - `Concept Drift`
    - CPD 알고리즘의 Parameter Tuning을 적용했으나, Human behavior는 Dynamic하므로 unseen pattern을 보이는 (학습 안한) data가 있을 수도 있다
    - Drift Detection and Update 방식을 추가하거나, Additional feature 혹은 method를 적용해볼 수도 있다.
  - `Change Point, 또는 Transition을 어떻게 정의할까`
    - SEP는 Feature Space에서의 Data distribution 변화를 감지하는 Unsupervised 방식이기 때문에, 우리가 이해하는 Transition과는 다른 change를 감지할 수도 있다.


내 생각: SEP 구현 과정에서 여전히 **View를 어떻게 설정할 것인지에 대한 의문점**이 있다.
  - **2-real time**이라는 것은 곧 **event *t+1* 과 *t+2* 를 현재 event *t*에 대한 CPD에 사용할 것**
  - 그렇다면 **view size *n*=2**라고 했으니, 
    1. **[feature *t*, feature *t+1*] 과 [feature *t+1*, feature *t+2*]** 을 비교한 Score가 event t의 dissimilarity score인가
    2. **[feature *t-1*, feature *t*] 과 [feature *t+1*, feature *t+2*]** 인가 **(지금은 이 방식대로 사용함)**
    3. **[feature *t-2*, feature *t-1*] 과 [feature *t+1*, feature *t+2*]** 인가
  - 그러나, **Consecutive** Window라는 말과 **Sliding** Window라는 말이 자꾸 헷갈린다
    - "Sliding" window라는 말 자체가 한 칸씩 움직이면서 window를 이동한다는 말 아닌가? 그렇다면 1이 맞는데..
  - 또 하나 드는 의문은 현재 event의 **"이전과 이후"**를 비교한다고 했는데, 그러면 1번이 아니고 2나 3이 말이 되는 것 아닌가.
      