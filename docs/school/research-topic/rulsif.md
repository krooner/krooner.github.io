---
layout: post
title: "RuLSIF"
parent: Research Topic
grand_parent: School
nav_order: 2
date:   2021-05-05 16:00:00 +0900
---
# Relative unconstrained Least-Squares Importance Fitting
{: .no_toc }

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

## 논문
---
_S. Aminikhanghahi and D. J. Cook, "[**Using change point detection to automate daily activity segmentation**]," 2017 IEEE International Conference on Pervasive Computing and Communications Workshops (PerCom Workshops), 2017, pp. 262-267, doi: 10.1109/PERCOMW.2017.7917569._
$\pm 5$

[**Using change point detection to automate daily activity segmentation**]: https://ieeexplore.ieee.org/document/7917569

## 문제 정의
---
* `Real-time`으로 행동 분할
* 행동 전환을 감지하는 방식으로 접근: Activity Transition Detection (ATD)
  * 변화점 감지 알고리즘 `Change Point Detection (CPD)` 을 활용 
* 실제 스마트 홈에서 발생된 센서 데이터 기반 `Ambient sensor-based`

## 문제가 중요한 이유
---
* `HAR` 에서 인지 모델을 잘 학습시키려면 `Activity Segmentation`이 중요함
  * Activity의 시작과 끝이 잘 described된 a set of stream segments가 필요하다
  * 각 segment는 서로 중첩되지 않는 단일 행동
* `Real-time HAR`에서는 인지 모델 학습과 인풋에 대한 결과 제공이 동시에 이루어져야 함. 
  * **Activity Recognition과 Activity Segmentation이 Parallel한 수행**
  * `Real-time Activity Segmentation`

## 문제 해결을 위한 기존 연구
---
* `pre-segmented data` 를 활용함: `real-time 방식이 아님`
* `Sliding window approach`: 행동의 시작부터 종료 지점까지 발생된 데이터를 포함하도록 window의 길이를 정함
  * `optimal window size를 구하는 것이 Challenge`
* `CPD-based approach` 
  * Supervised: transition/non-transition에 대한 binary classification
    * 여러 activity 간 boundary를 학습하여 multi-class classifier를 만듦
    * `possible transition type 수가 많아질수록 complex learning`
    * `extreme class imbalance 문제`
  * Unsupervised: prior training 없이 `data의 statistical feature` 활용
      * PCA, Eigenspace를 활용한 Semi-supervised 방식: `subject-specific data가 학습에 필요함`
      * minimized contrast with sliding window autocorrelation correctness: `Accelerometer 데이터만 사용한 uni-modal`
      * gestural AR using CPD: **RuLSIF - relative density-ratio estimator를 사용함**

## 제안 방법론
---
1. 데이터 수집: 단일 사용자가 거주하는 [`CASAS`] 스마트 홈 센서 데이터 
    - 13개의 행동, Door 센서와 Motion 센서 사용
    - 센서 데이터 형태: `date`, `time`, `sensorID`, `value`
2. `Event Feature` 추출: `Event-based Sliding window`
	  - 현재 센서 데이터의 `Event Feature`: 현재 데이터 포함 이전 30개의 센서 데이터
    - Feature 종류
      - 지속 시간 `Duration` 
      - 현재 데이터의 시간 `Latest Event Time` 
      - 가장 많이 발현된 센서 `Dominant Sensor` 
      - 각 센서별 발현 횟수 `Occurrence of each sensor` ( `N` )
      - 각 센서별 최근 발현 시간 `Last fired time of each sensor` ( `N` )
    - Feature Normalization: 각 feature를 [0, 1]로 변환
3. 행동 전환 감지 `Activity Transition Detection`
    - [`RuLSIF`] (Relative unconstrained Least-Squares Importance Fitting)
      - Two samples 간의 relative (probability) density-ratio를 계산
        - 계산된 ratio가 `threshold = 0.9`를 exceed하면 transition point
      - Dissimilarity Measure: `alpha-relative Pearson Divergence (PE)`
        - `alpha = 0.5, according to figure`
      - `*n*-real time` algorithm
          - CPD를 하려면 현재 event로부터 *n*개의 future events가 추가로 필요함
          - *n*=2
    - `BCPD` (Bayesian Change Point Detection)
      - 이전 Change Point Candidate 이후의 데이터와 현재 window의 확률 분포 비교
4. 전환점을 기준으로 나눈 행동 세그먼트 특징 추출 `Segment features`
	- ATD로 얻은 Change Points를 기준으로 stream을 자른 뒤 feature를 뽑아냄
5. 행동 인지 `Activity Recognition`
	- Decision Tree, Random Forest, Extra Trees, Gradient Boosting, Bagging, AdaBoost 등 다양한 Multi-class classifier를 가지고 Performance 측정

[`CASAS`]: http://casas.wsu.edu/datasets/
[`RuLSIF`]: https://riken-yamada.github.io/RuLSIF.html  
  
## 결과
---
Real transition event time으로부터 **$\pm$ 15초** 안에 candidate event가 있으면, 해당 event는 **true positive**

**RuLSIF는 BCPD와 fixed sliding window (baseline)보다 높은 ATD performance를 보임**

| | Baseline  | RuLSIF  | BCPD  |
|---|---|---|---|
| TPR  | 0.2  | **0.7**  | 0.4  |
| G-Mean  | 0.44  | **0.82**  | 0.62 |
| MAE  | 33.4  | **3.5**  | 7.0  |

HAR performance는 BCPD가 RuLSIF와 큰 차이가 없음
  - Accurate한 transition을 찾으려면 RuLSIF
  - activity의 전반적인 trend를 찾으려면 BCPD

## 의견
논문에서는 Non-parametric Kernel Model을 사용하기 때문에 `non-parametric` method라고 하지만, 정확히 말하면 사전에 주어진 parameter candidate list (e.g. $\lambda$ - regularization term, $\sigma$ - kernel parameter)로부터 optimal combination을 찾는 방식이다.

CASAS Dataset의 특성에 최적화된 parameter 이므로 다른 smart home dataset에 대해서도 성능이 보장되지 않을 것이다.
  - `window size` *30*
  - `view size` *n=2*
  - `minimum distance between transitions` *1*
  - `threshold value` *0.9*
  - `alpha` *0.5*

**Evaluation 방식에 대해, 개인적으로 드는 의문**

예를 들어 10000개의 events가 있고, 실제 transition은 100개라고 하자.
위와 같이 TPR이 0.7이고, G-Mean이 0.82면 FPR은 0.1 (1-TNR)정도 될 것이다.
  - `TPR` =  $\frac{TP}{P}$ = $\frac{TP}{TP+FN}$ =$\frac{70}{70+30}$ 
  - `FPR` =  $\frac{FP}{N}$ = $\frac{FP}{FP+TN}$ =$\frac{990}{9900}$
    - TP가 100개 이상이 될 수 있으나 ratio는 크게 안 벗어남.

*FP가 990개인데 어떻게 Segmentation을 하지?*

FP라는 것은 결국 Activity 중간 지점마다 위치한 Candidate (Wrong Detected Point)인데, 이 부분을 다 잘라버리면 Segment는 엉망진창이 될 것.
압도적으로 $P<<N$ 인 상황에서, 논문에서 말하듯이 FPR이 10%-15% 정도 된다는 것은 Wrong Detection Point가 수천-수만 개가 된다는 얘기고 이 지점들에서 전부 잘려버린다는 얘기인데, **정확도가 너무 안 좋은 것 같다.**

<!-- MathJax -->
<script type="text/javascript"
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>