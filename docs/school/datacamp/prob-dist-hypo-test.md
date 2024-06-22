---
title: "Distribution and Hypothesis"
layout: post
parent: DataCamp
grand_parent: 'School (2013-2022)'
date:   2022-03-23 21:03:00 +0900
last_modified_date: 2024-06-21
---
# 확률 분포와 가설 검정
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

연구자가 숫자를 사용하기 위해 데이터를 수량화하고 설명, 시각화, 통계 모델링하기 위한 도구로 통계를 이용한다

> 80명의 시험 성적 데이터에서 패턴 찾기
> 1. 도수분포표로 재배열한다
> 2. 히스토그램, 박스플롯으로 시각화한다
> 3. 정규성 테스트: 수집된 데이터에 대한 통계적 분석을 기반으로 추론
>   - Shapiro-wilk test ($w$, $p$-value) 학생 성적은 `정규분포`를 이룬다고 가정
>   - 정규곡선 아래, 전체 면적의 일정 비율은 $\mu$과 $\sigma$ 단위의 거리 사이에 놓인다

## 확률 분포

### Normal Distribution

정규성 테스트를 통해 데이터셋이 정규분포로 잘 모델링 되었는지 결정

> Shapiro-wilk test
> - $H_0$: Population이 정규 분포를 이룬다 - If $p\le\alpha$, reject $H_0$ (정규 분포가 아니다)
> - $H_a$: Population이 정규 분포를 이루지 않는다 - Otherwise, fail to reject $H_0$ (정규 분포를 이룬다)

평균의 샘플링 분포
- 샘플링 데이터는 전체를 충분히 대표하며 정확한 일반화가 가능하다; $\bar{X}$로부터 $\mu$ 를 추론
- Population: 우리가 알고 싶은 것, $(\mu, \sigma^2)$
- Sample: 우리가 분석하는 것, $(\bar{X}, s^2)$
- 평균의 샘플링 분포는 정규 분포에 근사하며, 평균의 샘플링 분포의 `mean`은 true population mean과 같다

신뢰 구간 (Confidence Interval, CI)
- 주로 95%의 신뢰 구간을 갖도록 계산된다. 평균의 표준 오차를 이용해서, $\mu$가 위치할 value range를 정한다
- unknown parameter에 대해 그럴듯한 (plausible) 범위를 제공하므로 가설 검정 결과보다 더 많은 정보를 준다
    1. $z$-score 계산
    2. If $z>1.96$, reject $H_0$. Otherwise, fail to reject $H_0$

$z$-score (standard score)
- 임의의 분포를 $\mu$로부터 $\sigma$의 집합으로 바꿀 수 있다
- raw score가 분포의 mean으로부터 얼마나 탈선했는지 direction과 degree를 알려준다

|신뢰 수준|$z$-score|
|---|---|
|68%|$z=\pm1.00$|
|95%|$z=\pm1.96$|
|99%|$z=\pm2.58$|

### t-Distribution
- `샘플 사이즈가 작을 때` 또는 $\sigma$를 모를 때 활용하며, 통계학자들은 $t$-score를 활용한다
- 샘플 평균 ($\bar{X}$)에 대한 신뢰 구간: $\bar{X}\pm t_{1-\frac{\alpha}{2},n-1}\frac{s}{\sqrt{n}}$
    - $s$: 샘플의 표준 편차
    - $n$: Observation 수 (샘플 데이터 수)
    - $t_{1-\frac{\alpha}{2},n-1}$: critical $t$-value
- Independent two-sample $t$-test 또는 Dependent $t$-test for paired samples가 있다.

Two-sample student's t-test
1. $H_{0}: \mu_1 = \mu_2$, $H_{a}: \mu_1 \neq \mu_2$
2. Significance Level $\alpha (=0.05)$, Confidence Level $1-\alpha (=0.95)$
3. $T=\frac{\bar{Y_1}-\bar{Y_2}}{\sqrt{\frac{S_{1}^{2}}{N_1}+\frac{S_{2}^{2}}{N_2}}}$
    - $N_1, N_2$: 샘플 크기
    - $\bar{Y_1}, \bar{Y_2}$: 샘플 평균
    - $s_{1}^{2}, s_{2}^{2}$: 샘플 분산
4. $p$-value를 계산한다: df (degree of freedom) = $N_1+N_2-2$
5. if $p\le\alpha$, reject $H_{0}$

## 가설 검정

가설이란 알려진 데이터에 대한 일관된 명제이며 아직 참인지 거짓인지 검증되지 않은 것. 주어진 가설이 참인 확률을 결정하기 위해 통계적으로 접근한다
- $H_{0}$, null hypothesis: 참이라는 가정 아래, Reject될 가능성을 검증하기 위한 통계 가설
- $H_{a}$, alternative hypothesis: $H_{0}$과 반대되며, 관찰 결과가 실제 효과로 나타날 때 채택된다

검증 방식
- $p$-value를 $\alpha$ (acceptable significance value)와 비교
- $p\le\alpha$이면 관찰된 effect는 통계적으로 유의미하다: $H_{0}$는 Reject되고 $H_{a}$가 Accept된다

> 유의 수준 $\alpha$
> - 통계에서 `significant` = `probably true` (`high significant` = `very probably true`)
> - $\alpha$는 $H_{0}$이 reject되고 $H_{a}$가 accept될 확률 수준으로 사회과학에서는 전통적으로 $\alpha=0.05$

### ANOVA (ANalysis Of Variance)

카테고리 독립 변수와 연속 종속 변수 간의 관계를 관찰하고, group mean 사이의 차이를 분석

|종류|설명|
|---|---|
|One-way ANOVA|쥐는 짝짓기 시기에 체중이 증가하나?|
|Two-way ANOVA|쥐는 짝짓기 시기에 체중이 증가하고, 이건 쥐의 성별에 의한 것인가?|

> One-way ANOVA: 분산을 이용하여 2개 이상의 mean의 일치함을 한번에 검증함
> - $H_0: \mu_1=\mu_2=...=\mu_k$
> - $H_a: \exist i, j ~\mu_i \neq \mu_j$

|Group|1|...|k|
|---|---|---|---|
||$x_{11}$|...|$x_{k1}$|
||...|...|...|
||$x_{1n_{1}}$|...|$x_{kn_{k}}$|
|**Group Mean**|$\mu_1$|...|$\mu_k$|

1. Mean difference를 관찰한다
2. fitted model에 대한 ANOVA table을 계산한다
3. $F$-test 결과를 분석한다
4. Tukey HSD (Honestly significant difference) Post-hoc test

> Two-way ANOVA: `하나의 연속 종속 변수`에 대한 `두 개의 서로 다른 카테고리 독립 변수의 영향`을 분석하며, 두 개의 요인 (A, B)과 종속 변수 (D)에 대한 가설을 검증한다.
> - Interaction effect $H_0:$ A, B 간 상호작용은 D에 유의한 영향을 주지 않는다
> - Main effect
>    - $A:$ A는 D에 유의한 영향을 주지 않는다
>    - $B:$ B는 D에 유의한 영향을 주지 않는다

남아와 여아의 나이 그룹별 (10, 11, 12세) 사칙 연산 검정 점수
- Factor 1: 성별 (남, 여)
- Factor 2: 나이 (10, 11, 12)

1. Main effect hypothesis
  - 성별 $H_0$ 성별은 학생 점수에 유의한 효과를 주지 않는다 / $H_a$
  - 나이 $H_0$ 나이는 학생 점수에 유의한 효과를 주지 않는다 / $H_a$
2. Interaction effect hypothesis
  - $H_0$ 성별과 나이의 상호작용은 학생 점수에 유의한 효과를 주지 않는다 / $H_a$

### Chi-square

적합도 검정 (Goodness of Fit): 관찰된 샘플 분포를 기대 확률 분포와 비교하기 위해 사용하며, 모집단 (Population)의 단일 카테고리 변수에 대해 적용하는 검정이다.
- $H_0$: 관찰값과 기댓값 사이에 유의한 차이가 없다 / $H_a$: 관찰값과 기댓값 사이에 유의한 차이가 있다
- $\chi^2$ 분포가 사용된다
    - $df=k-1$, $k$는 카테고리 수
    - $E=\frac{n}{k}$, $n$은 전체 frequency

$\chi^2=\sum_{i=1}^{n}\frac{(O_i - E_i)^2}{E_i}$
- $O_i$: 타입 $i$의 관찰된 frequency
- $E_i$: 타입 $i$의 기대 frequency

### 독립성 (Independence)

두 개 이상의 카테고리 변수 간의 통계적 독립을 검정한다 (Cross-tabulation analysis)

$\chi^2=\sum_{i=1}^{R}\sum_{j=1}^{C}\frac{(o_{ij}-e_{ij})^2}{e_{ij}}$
- $o_{ij}:$ observed cell count of $(i, j)$ element in table
- $e_{ij}:$ expected cell count of $(i, j)$ element in table ($e_{ij}=\frac{row_{i} total \times col_{j} total}{\text{grand total}}$)
- $o_{ij}-e_{ij}: $ residual of cell $(i, j)$

Contingency table (two-way tables, cross-tabulations)
- 두 카테고리 변수 데이터의 빈도 분포를 보이는데 활용됨
- $H_0:$ A와 B가 Independent / $H_a:$ A와 B가 Independent하지 않다
- $df = (r-1)\cdot(c-1)$

||B|total|
|---|---|---|
|**A**|||
|**total**||n|