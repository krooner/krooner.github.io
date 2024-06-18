---
title: "Regression Analysis"
layout: post
parent: Prob and Stat
grand_parent: School
nav_order: 4
date:   2022-03-23 21:03:00 +0900
---
# 회귀 분석
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 회귀
---
### 단일변량
Model
- $y=a+bx+\epsilon$

Least-square fit
- residuals $\epsilon_i=y_i-a-bx_i$
    - $a = \bar{y}-b\bar{x}$
    - $b = \frac{Cov(x, y)}{Var(x)}=\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^{n}(x_i-\bar{x})^2}$

Goodness of fit: 모델이 얼마나 관찰된 데이터를 잘 나타내는가
- $SS_{total}=\sum(Y-Y_{mean})^2$
- $SS_{residual}=\sum(Y-Y_{predicted})^2$
- $SS_{model} = \sum(Y_{predicted}-Y_{mean})^2 = SS_{total} - SS_{residual}$

R-squared $R^2=\frac{SS_{model}}{SS_{total}}=\frac{SS_T-SS_R}{SS_T}=1-\frac{SS_R}{SS_T}$
- coefficient of determination
- $0 ~(Good)\leq R^2 \leq 1 ~(Bad)$

### 다변량
$y=a_0+a_1 x_1+...+a_k x_k+\epsilon$
- $x_1,...,x_k:$ explanatory variables
- $a_0,...,a_k:$ estimated using least-squares method

## 로지스틱 회귀
---
### 단변량
$y=P(x)$
- $y:$ 종속 변수, 카테고리 (일반적으로 바이너리 - 0, 1)
- $x:$ 예측 변수, 연속/비율/구간/카테고리 모두 가능

$P(success\vert x) = \frac{e^{\beta_0+\beta_1x}}{1+e^{\beta_0+\beta_1x}}$

로지스틱 함수 
- $P(x) = \frac{1}{1+e^{-(\beta_0+\beta_1x)}}$

Odds $= \frac{P_{success}}{P_{failure}}=\frac{P}{1-P}=e^{\beta_0+\beta_1x}$
- odds가 클수록 success 확률이 높다

Odds ratio
- `특정 exposure가 주어졌을 때 결과가 발생할 odds`와 `주어지지 않았을 때 결과가 발생할 odds`의 비율
- $OR = \frac{odds(x+1)}{odds(x)} = e^{\beta_1}$

Logit (log of odds)
- value range를 $(-\infin, +\infin)$으로 확장
- $logit(p) = \ln\frac{p}{1-p} = \beta_0+\beta_1x$

예 - 시험 합격 여부와 공부 시간
- $logit(p) = \beta_0+\beta_1x=-4.0777+1.5046x$
- $OR = e^{1.5046} = 4.502557$
- 공부 한 시간 더했을 때의 odds는 그러지 않았을 때 odds보다 4.502557배 높다

### 다변량
$logit(p) = \beta_0+\beta_1x_1+...+\beta_k x_k$