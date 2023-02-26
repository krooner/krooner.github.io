---
title: "Artificial Intelligence"
layout: post
parent: Deep Learning
grand_parent: School
nav_order: 1
date:   2022-02-26 11:16:00 +0900
---
# 인공지능이란
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## AI in the wild
---
- 자율주행 (Waymo)
- 게임 (IBM Watson, AlphaGo)
- 추천 (YouTube, Google Ad)
- 보안 (얼굴 인식)
- 헬스케어 (엑스레이 이미지로 암 판별)
- 경제 (에너지 절약, 공급/수요 예측)
- 어시스턴트 (애플 시리, 구글 어시스턴트, grammarly)

## What is AI
---
지능 (Intelligence)
- 지각하고 (운전자는 시각 및 청각피질을 통해 바로 앞에 있는 현장을 관찰)
- 추론하고 (앞 사람은 아기 때문에 천천히 걷는다, 속도 제한이 있다, 방향 제한이 있다)
- 행동하고 (좌회전을 해야한다)
- 학습할 수 있는 능력 (좌회전이 아니라 우회전을 했어야 했다)

AI의 목표: 계산가능한 함수를 이용하여 지능의 구성요소를 모델링하는 것
- 지각 (Perception): 관찰한 것을 `기계가 이해할 수 있는` 형태로 변환
    - 음파 (Soundwave), 텍스트 (`Hello`), 이미지 (X-ray)
- 추론 (Reason): 데이터와 Output 사이의 맵핑 $f(x)$을 설계
- 행동 (Action): 태스크의 Output들을 정의
    - "피자 먹고 싶다", `안녕하세요`, 질병 진단 결과

AI (Artificial Intelligence)
- 컴퓨터가 인간 행동을 흉내낼 수 있도록 하는 기술

ML (Machine Learning)
- 명시적으로 프로그래밍되지 않고도 학습할 수 있는 능력
- $ML\subset AI$

ML의 워크플로우
- 전통적 패턴 인식: `입력값` - `특성 추출` - `학습 모델` - Loss
    - 특성 추출 과정은 hand-engineered (전문가에 의해 설계됨)
    - 이미지 (Bag-of-Words), 음파 (Fast Fourier Transform)
- 딥러닝: `입력값` - `저수준, 중수준, 고수준 특성` - `학습 모델` - Loss
    - 특성들은 전문가의 설계 없이 end-to-end 방식으로 학습될 수 있다

## 강의에서 배울 분야
---
- 이미지 이해: 이미지 분류, 물체 감지, 시멘틱 분할, 자세 추정
- 언어 이해: 기계 번역
- 음성 이해: 발화 인지
- 신경망 이해: 적대적 공격, 스타일 변환
- 생성적 모델링: 이미지, 텍스트, 음성 생성, 
    - 조건적 생성 모델링: 상호작용 생성
    - 비지도 조건적 생성 모델링: 모션 변환, 이미지 변환

