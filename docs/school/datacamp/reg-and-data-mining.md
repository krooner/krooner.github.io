---
title: "Regression and Data Mining"
layout: post
parent: DataCamp
grand_parent: 'School (2013-2022)'
date:   2022-03-23 21:03:00 +0900
last_modified_date: 2024-06-22
---
# 회귀분석과 데이터 마이닝
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 회귀 Regression

|변량|모델|설명|
|---|---|---|
|Univariate|$y=a+bx+\epsilon$|Least-square fit (최소제곱법): Residuals $\epsilon_i=y_i-a-bx_i$; $a = \bar{y}-b\bar{x}$, $b = \frac{Cov(x, y)}{Var(x)}=\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^{n}(x_i-\bar{x})^2}$|
|Multivariate|$y=a_0+a_1 x_1+...+a_k x_k+\epsilon$|$x_1,...,x_k:$ explanatory variables, $a_0,...,a_k:$ estimated using least-squares method|

Goodness of fit: 모델이 얼마나 관찰된 데이터를 잘 나타내는가
- $SS_{total}=\sum(Y-Y_{mean})^2$
- $SS_{residual}=\sum(Y-Y_{predicted})^2$
- $SS_{model} = \sum(Y_{predicted}-Y_{mean})^2 = SS_{total} - SS_{residual}$
- R-squared $R^2=\frac{SS_{model}}{SS_{total}}=\frac{SS_T-SS_R}{SS_T}=1-\frac{SS_R}{SS_T}$
  - Coefficient of determination; $0 ~(Good)\leq R^2 \leq 1 ~(Bad)$

### 로지스틱 회귀 Logistic Regression

|변량|모델|설명|
|---|---|---|
|Univariate|$y=P(x)$|$y:$ 종속 변수, 카테고리 (일반적으로 바이너리 - 0, 1), $x:$ 예측 변수, 연속/비율/구간/카테고리 모두 가능|
|Multivariate|$logit(p) = \beta_0+\beta_1x_1+...+\beta_k x_k$||

|용어|수식|설명|
|---|---|---|
|Logistic function|$P(x) = \frac{1}{1+e^{-(\beta_0+\beta_1x)}}$|$P(Success\vert x) = \frac{e^{\beta_0+\beta_1x}}{1+e^{\beta_0+\beta_1x}}$|
|Odds|$\frac{P_{success}}{P_{failure}}=\frac{P}{1-P}=e^{\beta_0+\beta_1x}$|Odds가 클수록 Success 확률이 높다.|
|Logit|$logit(p) = \ln\frac{p}{1-p} = \beta_0+\beta_1x$|log-of-odds를 의미하며 Value range를 $(-\infin, +\infin)$으로 확장|
|Odds ratio|$OR = \frac{odds(x+1)}{odds(x)} = e^{\beta_1}$|`특정 exposure가 주어졌을 때 결과가 발생할 odds`와 `주어지지 않았을 때 결과가 발생할 odds`의 비율|

> 시험 합격 여부와 공부 시간
> - $logit(p) = \beta_0+\beta_1x=-4.0777+1.5046x$
> - $OR = e^{1.5046} = 4.502557$
> - 공부 한 시간 더했을 때의 odds는 그러지 않았을 때 odds보다 4.502557배 높다

## 데이터 마이닝

|알고리즘|설명|
|---|---|
|Recursive Partitioning|모집단의 멤버를 정확히 분류하기 위한 Decision Tree를 만든다. 여러 이분법적 독립 변수들을 기반으로 서브 모집단들로 나눈다. 종료 조건에 도달할 때까지 서브 모집단이 유한하게 계속 분할된다 (`Recursive`)|
|Decision Tree|선택과 결과들을 트리 형태로 나타낸 그래프 $G=(V, E)$ ($V:$ 이벤트 또는 선택, $E:$ 의사결정 법칙 또는 조건) 또는 트리 (Root, Child nodes, Leaf)|

### 분할 알고리즘 및 종료 조건

분할 알고리즘
1. 현재 부분집합에 대한 RSS (Residual sum of squares) 계산
2. Item을 feature value 기준으로 정렬
3. 가능한 division에 대하여 $RSS_L$과 $RSS_R$을 계산하고, $\argmin_{L, R}[RSS_L+RSS_R]$을 찾아서 feature의 이름과 값을 반환

종료 조건
1. RSS = 0
2. 현재 부분집합의 element 수가 $r$개 이하이다; $r$을 너무 작게 설정하는 경우 과적합이 발생할 수 있다

### Regression/Classification Tree

재귀적인 예측 변수에 대한 binary split으로, Decision Tree는 회귀와 분류 모두 수행할 수 있음
- 회귀 나무: 1개 이상의 연속/카테고리 예측 변수로부터 `연속 종속 변수` 값을 예측할 때 사용
- 분류 나무: 1개 이상의 연속/카테고리 예측 변수로부터 `카테고리 종속 변수` 값을 예측할 때 사용

### Clustering

동종의 하위 그룹 (클러스터)를 만든다. 동일 클러스터에 있는 요소끼리는 다른 클러스터 요소들보다 서로 유사하다. 자동으로 데이터에서 패턴을 찾아주므로 데이터 마이닝과 빅데이터에 유용하다; Partitioning and Hierarchical

> 최적 클러스터 갯수: Partitioning clustering의 가장 근본적인 이슈로, 정답은 없다. (Rule of thumbs: modularity, elbow method, silhouette, gap statistics)

#### Partitioning Clustering

유사도를 기반으로 Item을 다수의 그룹으로 분류한다.
1. K-means
2. K-medoids (PAM, Partitioning Around Medoids)
3. CLARA (Clustering Large Analysis)

K-means
- $SS(k) = \sum_{i=1}^{n}\sum_{j=1}^{p}(x_{ij}-\bar{x}_{kj})$를 최소화
    - $k:$ 클러스터
    - $x_{ij}:$ $j$번째 변수, $i$번째 데이터 값
    - $\bar{x}_{kj}:$ $k$번째 클러스터에 대해 $j$번째 변수의 평균
- 문제점: 카테고리 데이터에 적용이 불가능하다. Outlier에 의해 영향받기 쉽다.
- K-means는 centroid (주로 가상의 데이터 포인트) 기준이며 K-medoids는 medoids (실제 데이터 포인트) 기준

#### Hierarchical clustering

Agglomerative (Bottom-up) 과 Divisive (Top-down) 으로 나뉘며 연산량이 많아서 주로 agglomerative 방식으로 접근한다.

### Association Rule

장바구니 분석 (Market Basket Analysis)이라고도 하며, 거대 데이터셋에 숨겨진 knowledge나 필요한 정보를 발견하는데 유용하다. 적용 분야는 제품 추천, 도서관 대여 서비스, 음악 추천, 의료 진단, 컨텐츠 최적화 등이다.

Itemset: 데이터셋 내 1개 이상의 item 집합
- Support $A\rightarrow B = \frac{A, B \text{ 둘 다 있는 데이터}}{\text{전체 데이터}}$
- Confidence $A\rightarrow B = \frac{Support (A\rightarrow B)}{Support(A)}$
- Lift $A\rightarrow B = \frac{Support (A\rightarrow B)}{Support(A)\cdot Support(B)}$