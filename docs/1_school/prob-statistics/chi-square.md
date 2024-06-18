---
title: "Chi-square Tests"
layout: post
parent: Prob and Stat
grand_parent: School
nav_order: 3
date:   2022-03-23 15:41:00 +0900
---
# Chi-square Tests
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 적합도 검정 (Goodness of Fit)
---
관찰된 샘플 분포를 기대 확률 분포와 비교하기 위해 사용되며, 모집단 (Population)의 단일 카테고리 변수에 대해 적용하는 검정
- $H_0$: 관찰값과 기댓값 사이에 유의한 차이가 없다
- $H_a$: 관찰값과 기댓값 사이에 유의한 차이가 있다
- $\chi^2$ 분포가 사용된다
    - $df=k-1$, $k$는 카테고리 수
    - $E=\frac{n}{k}$, $n$은 전체 frequency

$\chi^2=\sum_{i=1}^{n}\frac{(O_i - E_i)^2}{E_i}$
- $O_i$: 타입 $i$의 관찰된 frequency
- $E_i$: 타입 $i$의 기대 frequency

## 독립성 (Independence)
---
두 개 이상의 카테고리 변수 간의 통계적 독립을 검정한다 (Cross-tabulation analysis)

$\chi^2=\sum_{i=1}^{R}\sum_{j=1}^{C}\frac{(o_{ij}-e_{ij})^2}{e_{ij}}$
- $o_{ij}:$ observed cell count of $(i, j)$ element in table
- $e_{ij}:$ expected cell count of $(i, j)$ element in table
    - $e_{ij}=\frac{row_{i} total \times col_{j} total}{\text{grand total}}$
- $o_{ij}-e_{ij}: $ residual of cell $(i, j)$

Contingency table (two-way tables, cross-tabulations)
- 두 카테고리 변수 데이터의 빈도 분포를 보이는데 활용됨
- $H_0:$ A와 B가 Independent
- $H_a:$ A와 B가 Independent하지 않다
- $df = (r-1)\cdot(c-1)$

||B|total|
|---|---|---|
|**A**|||
|**total**||n|

