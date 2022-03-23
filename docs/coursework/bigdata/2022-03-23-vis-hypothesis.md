---
title: "데이터 시각화 / 확률, 분포, 가설 검정"
layout: post
parent: Introduction to Bigdata
grand_parent: Coursework
nav_order: 2
date:   2022-03-23 15:01:00 +0900
---
# Data Visualization / Probability, Distribution, and Hypothesis Test
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 데이터 시각화
---
- 의사결정자들이 통계를 시각적으로 보면서, 어려운 개념을 이해하고 새로운 패턴을 찾을 수 있다
- 데이터를 다른 관점에서 창의적으로 보며 더 많은 인사이트를 발견할 수 있다

종류
- Line, Scatter plot
- Barplot
    - Simple
    - Grouped
    - Matrix/table data
- Pie chart
- Histogram
- Bubble plots
- Boxplot
    - numerical data의 사분위 (quartile) 값으로 group을 표현함
- 3D Plots

## 확률, 분포, 가설 검정
---
랜덤 샘플링

정규 분포
- 정규성 테스트: 데이터셋이 정규분포로 잘 모델링 되었는지 결정
- Shapiro-wilk test
    - $H_0$: Population이 정규 분포를 이룬다
    - $H_a$: Population이 정규 분포를 이루지 않는다
- If $p\le\alpha$, reject $H_0$ (정규 분포가 아니다)
- Otherwise, fail to reject $H_0$ (정규 분포를 이룬다)

평균의 샘플링 분포
- 샘플링된 멤버들은 전체 데이터를 충분히 대표한다
    - 전체에 대한 정확한 일반화가 가능하다
- Population: 우리가 알고 싶은 것, $(\mu, \sigma^2)$
- Sample: 우리가 분석하는 것, $(\bar{X}, s^2)$
    - $\bar{X}$로부터 $\mu$를 추론
- 평균의 샘플링 분포는 정규 분포에 근사한다
- 평균의 샘플링 분포의 `mean`은 true population mean과 같다

신뢰 구간 (Confidence Interval, CI)
- 주로 95%의 신뢰 구간을 갖도록 계산된다
- 평균의 표준 오차를 이용해서, $\mu$가 위치할 value range를 정한다
- unknown parameter에 대해 그럴듯한 (plausible) 범위를 제공하므로 가설 검정 결과보다 더 많은 정보를 준다
    1. $z$-score 계산
    2. If $z>1.96$, reject $H_0$
    3. Otherwise, fail to reject $H_0$

|신뢰 수준|$z$-score|
|---|---|
|68%|$z=\pm1.00$|
|95%|$z=\pm1.96$|
|99%|$z=\pm2.58$|

$t$-분포
- `샘플 사이즈가 작을 때` 또는 $\sigma$를 모를 때
- 통계학자들은 $t$-score를 활용한다
- 샘플 평균 ($\bar{X}$)에 대한 신뢰 구간: $\bar{X}\pm t_{1-\frac{\alpha}{2},n-1}\frac{s}{\sqrt{n}}$
    - $s$: 샘플의 표준 편차
    - $n$: Observation 수 (샘플 데이터 수)
    - $t_{1-\frac{\alpha}{2},n-1}$: critical $t$-value

Independent two-sample $t$-test

Dependent $t$-test for paired samples