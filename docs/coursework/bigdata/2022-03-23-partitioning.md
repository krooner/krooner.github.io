---
title: "재귀 분할, 클러스터링, 연관 분석"
layout: post
parent: Introduction to Bigdata
grand_parent: Coursework
nav_order: 5
date:   2022-03-23 21:35:00 +0900
---
# Recursive Partitioning / Clustering / Association Rule
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


## Recursive Partitioning
---
모집단의 멤버를 정확히 분류하기 위한 Decision Tree를 만듦
- 여러 이분법적 독립 변수들을 기반으로 서브 모집단들로 나눔
- `Recursive` - 종료 조건 도달할 때까지 서브 모집단이 유한하게 계속 분할됨

### Decision Tree
선택과 결과들을 트리 형태로 나타낸 그래프
- 그래프 $G=(V, E)$
    - $V:$ 이벤트 또는 선택
    - $E:$ 의사결정 법칙 또는 조건
- 트리
    - Root
    - Child nodes (Decision nodes)
    - Leaf

### 분할 알고리즘과 종료 조건
분할 알고리즘
1. 현재 부분집합에 대한 RSS (Residual sum of squares) 계산
2. Item을 feature value 기준으로 정렬
3. 가능한 division에 대하여 $RSS_L$과 $RSS_R$을 계산하고, $\argmin_{L, R}[RSS_L+RSS_R]$을 찾아서 feature의 이름과 값을 반환

종료조건
1. RSS = 0
2. 현재 부분집합의 element 수가 $r$개 이하이다
    - $r$을 너무 작게 설정하는 경우 과적합이 발생할 수 있다

### 회귀 나무와 분류 나무
재귀적인 예측 변수에 대한 binary split으로, Decision Tree는 회귀와 분류 모두 수행할 수 있음

- 회귀 나무
    - 1개 이상의 연속/카테고리 예측 변수로부터 연속 종속 변수 값을 예측할 때 사용
- 분류 나무
    - 1개 이상의 연속/카테고리 예측 변수로부터 카테고리 종속 변수 값을 예측할 때 사용

## 클러스터링
---
분석 목적: 동종의 하위 그룹 (클러스터)를 만든다
- 동일 클러스터에 있는 요소끼리는 다른 클러스터 요소들보다 서로 유사하다
- 자동으로 데이터에서 패턴을 찾아주므로 데이터 마이닝과 빅데이터에 유용하다
    1. Partitioning
    2. Hierarchical

### 최적 클러스터 갯수
Partitioning clustering의 가장 근본적인 이슈로, 정답은 없다
- rule of thumbs: modularity, elbow method, silhouette, gap statistics

### Partitioning clustering
유사도를 기반으로 item을 다수의 그룹으로 분류
1. K-means
2. K-medoids (PAM, Partitioning Around Medoids)
3. CLARA (Clustering Large Analysis)

K-means
- $SS(k) = \sum_{i=1}^{n}\sum_{j=1}^{p}(x_{ij}-\bar{x}_{kj})$를 최소화
    - $k:$ 클러스터
    - $x_{ij}:$ $j$번째 변수, $i$번째 데이터 값
    - $\bar{x}_{kj}:$ $k$번째 클러스터에 대해 $j$번째 변수의 평균
- 문제점
    1. 카테고리 데이터에 적용 불가
    2. outlier에 의해 영향받기 쉬움

K-medoids
- medoids (실제 데이터 포인트를 기준으로)
- (K-means는 centroid - 주로 가상의 데이터 포인트)

### Hierarchical clustering
- agglomerative: Bottom-up
- divisive: Top-down
    - 연산량이 많아서 주로 agglomerative 방식으로 접근함

## Association Rule
---
장바구니 분석 (Market Basket Analysis)이라고도 하며, 거대 데이터셋에 숨겨진 knowledge나 필요한 정보를 발견하는데 유용하다
- `If-Then` 구조
- 적용 분야: 제품 추천, 도서관 대여 서비스, 음악 추천, 의료 진단, 컨텐츠 최적화

Itemset: 데이터셋 내 1개 이상의 item 집합
- Support $A\rightarrow B = \frac{A, B \text{ 둘 다 있는 데이터}}{\text{전체 데이터}}$
- Confidence $A\rightarrow B = \frac{Support (A\rightarrow B)}{Support(A)}$
- Lift $A\rightarrow B = \frac{Support (A\rightarrow B)}{Support(A)\cdot Support(B)}$