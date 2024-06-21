---
layout: post
title:  "Data Visualization"
parent: DataCamp
grand_parent: 'School (2013-2022)'
date:   2022-02-22 13:55:00 +0900
last_modified_date: 2024-06-21
---
# 데이터 시각화란
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

데이터로부터 Insight를 얻는 세 가지 방법
- `통계 (Summary statistics; 평균, 중앙값, 표준편차)`
- `모델 실행 (선형 회귀, 로지스틱 회귀)`
- `Plot 그리기 (Scatter, Bar, Histogram)`

> [Datasaurus Dozen](https://www.autodeskresearch.com/publications/samestats) 데이터셋은 `away`, `bullseye` 등 각 데이터셋은 `(x, y)` 좌표 데이터로 구성되어 있다. 각 데이터셋의 `mean(x)`, `mean(y)`, `std(x)`, `std(y)`는 모두 동일하지만 분포는 모두 다르다.

|away_x|away_y|bullseye_x|bullseye_y|...|x_shape_x|x_shape_y|
|---|---|---|---|---|---|---|
|32.33|61.41|51.20|83.34|...|38.34|92.47|
|53.42|26.19|58.97|85.50|...|35.75|94.12|
|...|...|...|...|...|...|...|
|63.92|30.83|51.87|85.83|...|32.77|88.52|

> 연속 변수와 카테고리 변수
> - **연속 변수** (주로 숫자): 높이, 온도, 수익 등
> - **카테고리 변수** (주로 텍스트): 나이 (20세) 는 연속 변수이지만, 연령대 (20-29세) 는 카테고리 변수. 시간은 연속 변수이지만, 월 (month)은 카테고리 변수

## Histogram

Histogram을 사용하는 이유로는 단일 연속 변수 데이터를 표현하는 경우와 데이터 분포 형태를 분석하려는 경우가 있다; 영국의 왕 (Kings and Queens)들의 집권 시작 당시 나이 (age at start of rule)에 따른 Histogram

|특징|설명|
|---|---|
|binwidth|하나의 bar에 포함되는 데이터 값의 범위. 너무 짧으면 전체 데이터가 많은 bin으로 나눠지게 됨. 너무 긴 경우에는 분명히 다른 분류로 취급되어야 할 데이터끼리 같은 bin에 속하게 되어 두 경우 모두 데이터 분포를 해석하기 어려우므로, 적절한 binwidth를 설정해야 한다.|
|modality|peak의 수. `unimodal, bimodal, trimodal, ...`|
|skewness|extreme value의 수. `left-skewed`: Histogram 왼쪽이 꼬리 (tail, 데이터가 거의 없음)이고 오른쪽에 데이터가 치우친 경우, `symmetric` (Histogram이 축을 기준으로 대칭인 형태), `right-skewed` (Histogram 오른쪽이 꼬리이고 왼쪽에 데이터가 치우친 경우)|
|kurtosis|데이터 분포의 뾰족한 정도. `leptokurtic` 분포의 형태가 평균을 중심으로 뾰족하게 모인 경우, `mesokurtic` 분포의 형태가 정규분포 모양과 유사한 경우, `platykurtic` 분포의 형태가 평균을 중심으로 넓게 펼쳐진 경우|

## Boxplot

Boxplot을 사용하는 이유로는 (카테고리 변수로 분할할 수 있는) 연속 변수를 표현하는 경우나 각 카테고리마다 연속 변수의 분포를 비교하려는 경우가 있다.

|특징|해석|
|---|---|
|mid-line|중앙값|
|box|`lower quartile (LQ)` (1/4분위수), `upper quartile (UQ)` (3/4분위수), `Inter-quartile range (IQR)`: `LQ`와 `UQ` 사이 범위|
|whisker|`lower whisker` (`LQ - 1.5*IQR` 보다 큰 값 중 최솟값), `upper whisker` (`UQ + 1.5*IQR` 보다 작은 값 중 최댓값)|

## Scatterplot

Scatterplot을 사용하는 이유로는 두 개의 카테고리 변수를 표현하려는 경우나 두 카테고리 변수 간의 관계를 분석하려는 경우가 있다.

> 예 - LA County의 집값; 집값 (Price)과 평수 (Area)의 관계를 Price를 log-scale로 표현할 수 있다.

|city|n_beds|price_musd|area_sqft|
|---|---|---|---|
|Long Beach|1|0.3250|846|
|Beverly Hills|3|2.1950|2930|
|...|...|...|...|
|Westwood|3|0.6950|1913|

> 상관관계 Correlation
> 1. Strong negative: 군집되어 직선을 이루고 기울기가 음수
> 2. Weak negative: 분산되어 직선을 이루고 기울기가 음수
> 3. No: 직선을 이루지 않음
> 4. Weak positive: 분산되어 직선을 이루고 기울기가 양수
> 5. Strong positive: 군집되어 직선을 이루고 기울기가 양수

|Plot|설명|
|---|---|
|Lineplot|두 개의 카테고리 변수 데이터가 있을 때. 두 변수 사이의 관계를 분석해야 할 때. 연속된 데이터끼리 연결되어 있을 때. 대부분의 경우 $x$축은 날짜 또는 시간일 때|
|Barplot|단일 카테고리 변수 데이터가 있을 때. 카테고리 별 횟수 또는 퍼센트를 계산해야 할 때.|
|Stacking bar|[어린이들의 과일/채소 소비량](https://digital.nhs.uk/data-and-information/publications/statistical/health-survey-for-england/2018/health-survey-for-england-2018-data-tables) 전체 대비 섭취량에 따른 어린이 구성 퍼센트|
|Dotplot|카테고리 변수 데이터가 있을 때. 각 카테고리에 대한 점수를 나타내야 (log-scale로 나타내거나, 여러 점수들을 나타내는 경우) 할 때.|
|Pairplot|연속 변수든 카테고리 변수든 최대 10개의 변수가 있다. 각 변수의 분포를 표현해야 한다. 각 변수 쌍 사이의 관계를 분석한다.|
|Correlation heatmap|많은 카테고리 변수 데이터가 있다. 각 변수 쌍 사이의 연관관계를 간단한 Overview로 보고싶다.|
|Parallel coordinates|많은 연속 변수 데이터가 있다. 변수들 간의 패턴을 찾거나 데이터의 클러스터를 시각화한다.|
|Polar coordinates|하루 중 시간 또는 나침반 방향 같이 Circular한 특성을 갖는 변수를 갖는 경우 가끔 사용함. 극좌표를 활용한 방식으로는 Pie plots (`Bar plot` + `Polar coordinates`) 와 Rose plots (`Histogram` + `Polar coordinates`) 가 있다.|

## High Dimension Visualization

$(x, y)$가 (평균 학교 교육 기간, 1인당 국민소득)이라고 할 때, `평균 수명`이라는 카테고리를 표현하려고 한다.

Scatterplot
1. New axis: ~~데이터를 해석하기 어려워진다~~
2. Color: 평균 수명 (<60 파랑), (60-70 녹색), (70-80 노랑)
3. Size: 평균 수명 (<60 Small), (60-70 M), (70-80 L)
4. Transparency: 평균 수명 (<60 0.1), (60-70 0.5), (70-80 0.9)
5. Shape: 평균 수명 (<60 원), (60-70 세모), (70-80 네모)
6. Multiple graphs: N개의 연령대 각각에 대한 그래프

Lineplot
1. Color: 카테고리 별 multiple lines
2. Linetype: Solid, dashes, Dotted, ...
3. Thickness
4. Transparency

### Colorscale의 세 가지 종류

|종류|목적|변화시킬 특성|예시|
|---|---|---|---|
|Qualitative|정렬되지 않은 카테고리 분류|Hue|각 카테고리 (자동차, 냉장고, 스토브, 청소기)의 연도별 adoption 퍼센트|
|Sequential|순서 표현|Chroma 또는 Luminance|Bar plots > Stacking bars 참조|
|Diverging|기준점 이상 또는 이하 표현|H,C,L|[친환경 기술에 대한 말레이시아 여론조사](http://dx.doi.org/10.17632/wggvryfhsk.1)|

> Colorspaces
> - RGB (Red-Green-Blue) 또는 CMYK (Cyan-Magenta-Yellow-blacK); Color를 고를 때, 현재 Color와 다음 Color 간의 `perceptual distance`은 일정해야 한다.
> - HCL (Hue-Chroma-Luminance); Hue, Chroma (Hue의 맑고 탁한 정도), Luminance (밝기)

## 좋은 시각화란

Plot에서 독자가 얼마나 많은 insight를 얻을 수 있는가? 얼마나 빠르게 독자가 insight를 획득할 수 있는가?
- 주의사항: 값 차이에 비례하게 시각화해야 하며, 가급적 2개의 축을 같은 방향으로 plot (Dual axes) 하지 않고 multiple panel로 표현한다.
- Chartjunk: 독자의 insight 획득을 방해하는 요소. 그림, Skueomorphism (반사, 그림자 등), 추가적인 dimension, Ostentatious colors, lines (불필요) 등이 있다.