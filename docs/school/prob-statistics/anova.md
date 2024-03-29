---
title: "Analysis of Variance"
layout: post
parent: Prob and Stat
grand_parent: School
nav_order: 4
date:   2022-03-23 21:03:00 +0900
---
# ANOVA
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

카테고리 독립 변수와 연속 종속 변수 간의 관계를 관찰하고, group mean 사이의 차이를 분석

### One-way ANOVA
분산을 이용하여 2개 이상의 mean의 일치함을 한번에 검증함
- $H_0: \mu_1=\mu_2=...=\mu_k$
- $H_a: \exist i, j ~\mu_i \neq \mu_j$

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

### Two-way ANOVA
한 연속 종속 변수에 대한, 두 개의 서로 다른 카테고리 독립 변수의 영향을 분석

비교
- One-way ANOVA: 쥐는 짝짓기 시기에 체중이 증가하나?
- Two-way ANOVA: 쥐는 짝짓기 시기에 체중이 증가하고, 이건 쥐의 성별에 의한 것인가?
    - 두 개의 요인 (A, B)과 종속 변수 (D)에 대한 가설
    - Interaction effect $H_0:$ A, B 간 상호작용은 D에 유의한 영향을 주지 않는다
    - Main effect
        - $A:$ A는 D에 유의한 영향을 주지 않는다
        - $B:$ B는 D에 유의한 영향을 주지 않는다

예 - 남아와 여아의 나이 그룹별 (10, 11, 12세) 사칙 연산 검정 점수
- Factor 1: 성별 (남, 여)
- Factor 2: 나이 (10, 11, 12)

1. Main effect hypothesis
    - 성별
        - $H_0:$ 성별은 학생 점수에 유의한 효과를 주지 않는다
        - $H_a$
    - 나이
        - $H_0:$ 나이는 학생 점수에 유의한 효과를 주지 않는다
        - $H_a$
2. Interaction effect hypothesis
    - $H_0:$ 성별과 나이의 상호작용은 학생 점수에 유의한 효과를 주지 않는다
    - $H_a$