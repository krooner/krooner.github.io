---
title: "Statistics"
layout: post
parent: Prob and Stat
grand_parent: School
nav_order: 1
date:   2022-03-23 11:16:00 +0900
---
# 통계의 활용
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

연구자가 숫자를 사용할 때
- 데이터를 수량화한다
- 설명, 시각화, 통계 모델링하기 위한 도구로 통계를 이용한다

예 - 80명의 시험 성적 데이터에서 패턴 찾기
1. 도수분포표로 재배열한다
2. 히스토그램, 박스플롯으로 시각화한다
3. 정규성 테스트: 수집된 데이터에 대한 통계적 분석을 기반으로 추론
    - Shapiro-wilk test ($w$, $p$-value)
    - 학생 성적은 `정규분포`를 이룬다.

정규곡선
- 정규곡선 아래, 전체 면적의 일정 비율은 $\mu$과 $\sigma$ 단위의 거리 사이에 놓인다

$z$-score (standard score)
- 임의의 분포를 $\mu$로부터 $\sigma$의 집합으로 바꿀 수 있다
- raw score가 분포의 mean으로부터 얼마나 탈선했는지 direction과 degree를 알려준다

가설 검증
- 가설: 알려진 데이터에 대한 일관된 명제, 아직 참인지 거짓인지 검증되지 않음
- 주어진 가설이 참인 확률을 결정하기 위해 통계적으로 접근한다
  - $H_{0}$, null hypothesis: 참이라는 가정 아래, Reject될 가능성을 검증하기 위한 통계 가설
  - $H_{a}$, alternative hypothesis: $H_{0}$과 반대되며, 관찰 결과가 실제 효과로 나타날 때 채택된다
- 검증 방식
  - $p$-value를 $\alpha$ (acceptable significance value)와 비교
  - $p\le\alpha$이면 관찰된 effect는 통계적으로 유의미하다
    - $H_{0}$는 Reject되고 $H_{a}$가 Accept된다

유의 수준 $\alpha$
- 통계에서 `significant` = `probably true`
- `high significant` = `very probably true`
- $\alpha$는 $H_{0}$이 reject되고 $H_{a}$가 accept될 확률 수준
  - 사회과학에서는 전통적으로 $\alpha=0.05$

Two-sample student's t-test
1. $H_{0}: \mu_1 = \mu_2$, $H_{a}: \mu_1 \neq \mu_2$
2. Significance Level $\alpha (=0.05)$
    - Confidence Level $1-\alpha (=0.95)$
3. $T=\frac{\bar{Y_1}-\bar{Y_2}}{\sqrt{\frac{S_{1}^{2}}{N_1}+\frac{S_{2}^{2}}{N_2}}}$
    - $N_1, N_2$: 샘플 크기
    - $\bar{Y_1}, \bar{Y_2}$: 샘플 평균
    - $s_{1}^{2}, s_{2}^{2}$: 샘플 분산
4. $p$-value를 계산한다
    - df (degree of freedom) = $N_1+N_2-2$
5. if $p\le\alpha$, reject $H_{0}$