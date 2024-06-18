---
layout: post
title:  "Adv. Query and CTE"
parent: Database
grand_parent: School
nav_order: 6
date:   2022-02-15 14:51:00 +0900
---
# 상관 및 중첩 쿼리와 공통 테이블 식
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 상관 쿼리 (Correlated Subquery)
---
결과를 생성하기 위해 외부 (Outer) 쿼리의 값을 사용하며, 최종 데이터셋에서 생성되는 모든 행에 대해 재실행됨.
- Advanced Joining, filtering and evaluating data에 사용됨.

### Simple VS Correlated
Simple subquery는 메인 쿼리와 독립적으로 수행되며, 전체 쿼리에서 한번만 실행된다.

Correlated subquery는 메인 쿼리에 의존적이며, 반복적으로 (in loops) 실행되므로 **쿼리 실행시간을 크게 증가시킨다**.

예 - 각 나라별 평균 득점 수

```sql
SELECT
  c.name AS country,
  (SELECT
     AVG(home_goal + away_goal)
   FROM match AS m
   WHERE m.country_id = c.id)
     AS avg_goals
FROM country AS c
GROUP BY country;
```

OUTPUT

| country     | avg_goals        |
|-------------|------------------|
| Belgium| 2.89344262295082 |
| England| 2.76776315789474 |
| France| 2.51052631578947 |
| Germany| 2.94607843137255 |
| Italy| 2.63150867823765 |
| Netherlands | 3.14624183006536 |
| Poland|2.49375|
| Portugal|2.63...|
| Scotland|2.74...|
| Spain|2.78|
| Switzerland | 2.81054131054131 |

예 - 2012/13 시즌 라운드 별 평균 득점을 초과한 라운드 및 득점 수

```sql
SELECT
    s.stage,
    ROUND(s.avg_goals,2) AS avg_goal,
    (SELECT AVG(home_goal + away_goal)
     FROM match
     WHERE season = '2012/2013') AS overall_avg
FROM
    (SELECT
         stage,
         AVG(home_goal + away_goal) AS avg_goals
     FROM match
     WHERE season = '2012/2013'
     GROUP BY stage) AS s
WHERE s.avg_goals > (SELECT AVG(home_goal + away_goal)
                     FROM match AS m
                     WHERE s.stage > m.stage);
```

OUTPUT

| stage | avg_goals |
|-------|-----------|
|3 | 2.83 |
|4 |2.8 |
|6 | 2.78 | 
|8 | 3.09 | 
|10 |2.96 |

## 중첩 쿼리 (Nested Subquery)
---
또 다른 서브쿼리 내의 서브쿼리로, 데이터 변형 (Transformation)이 여러 번 (multiple layers) 수행된다.

예 - (월별 총 득점 수 - 월별 평균 총 득점)

```sql
SELECT
  EXTRACT(MONTH FROM date) AS month,
  SUM(m.home_goal + m.away_goal) AS total_goals,
  SUM(m.home_goal + m.away_goal) -
  (SELECT AVG(goals) -- outer subquery
   FROM (SELECT -- inner subquery
           EXTRACT(MONTH FROM date) AS month,
           SUM(home_goal + away_goal) AS goals
         FROM match
         GROUP BY month) AS s) AS diff
FROM match AS m
GROUP BY month;
```

OUTPUT

| month | goals | diff     |
|-------|-------|----------|
|01 |5821 |-36.25 |
|02 | 7448 | 1590.75 |
|03 | 7298 | 1440.75 |
|04 | 8145 | 2287.75 |

## 상관 및 중첩 쿼리 (Correlated nested subqueries)
---
예 - 2011/12 시즌 각 나라별 평균 득점 수

```sql
SELECT
  c.name AS country,
  (SELECT AVG(home_goal + away_goal)
   FROM match AS m
   WHERE m.country_id = c.id -- Correlates with main query
         AND id IN (
             SELECT id -- Begin inner subquery
             FROM match
             WHERE season = '2011/2012')) AS avg_goals
FROM country AS c
GROUP BY country;
```

OUTPUT

| country     | avg_goals        |
|-------------|------------------|
| Belgium| 2.87916666666667 |
| England| 2.80526315789474 |
| France| 2.51578947368421 |
| Germany| 2.85947712418301 |
| Italy| 2.58379888268156 |
| Netherlands | 3.25816993464052 |
| Poland|2.1958..|
| Portugal|2.6417..|
| Scotland|2.6359..|
| Spain|2.7631...|
| Switzerland | 2.62345679012346 |

## Common Table Expressions (CTE)
---
서브쿼리를 추가할 때, Query complexity는 빠르게 증가하기 때문에 필요한 정보를 트래킹하기 어려워질 수 있다.
1. 메인 쿼리 이전에 선언되는 테이블
2. `FROM` 문에서 명명되고 참조됨

CTE를 쓰는 이유
1. 한번만 실행됨: 메모리에 저장되어 쿼리 성능을 향상시킴
2. 쿼리 구성 (Organization of queries)을 향상시킴
3. 다른 CTE를 참조하고, 자기 자신을 참조 (Self-join)할 수도 있음

```sql
WITH cte AS (
    SELECT col1, col2
    FROM table)
SELECT
    AVG(col1) AS avg_col
FROM cte;
```

예 - 국가별 경기 득점이 10골 이상인 경기과 1골 이하인 경기 수

```sql
WITH s1 AS (
  SELECT country_id, id
  FROM match
  WHERE (home_goal + away_goal) >= 10),
s2 AS (
  SELECT country_id, id
  FROM match
  WHERE (home_goal + away_goal) <= 1
)

SELECT
  c.name AS country,
  COUNT(s1.id) AS high_scores,
  COUNT(s2.id) AS low_scores
FROM country AS c
INNER JOIN s1
ON c.id = s1.country_id
INNER JOIN s2
ON c.id = s2.country_id
GROUP BY country;
```

## 정리
---
### JOIN
두 개 이상의 테이블을 결합하여, 간단한 Operation/aggregation을 수행
> `직원` 당 전체 `판매량`은?

### Correlated Subqueries
서브쿼리와 테이블을 매칭하여 JOIN의 한계를 개선하지만, 처리 시간이 많이 소요됨
> `회사`에서 각 `직원`은 누구에게 보고하는가?

### Nested Subqueries
다단계 변형을 통하여 정확성과 재생산성을 향상시킴
> 해당 분기의 각 영업 담당자에 의해 마감된 평균 거래 규모는?

### CTE
서브쿼리를 순차적으로 조직하며, 다른 CTE를 참조할 수 있다.
> 마케팅, 영업, 성장 및 엔지니어링 팀이 주요 지표에서 어떤 성과를 냈습니까?

주어진 DB와 해결할 문제에 따라 다르지만, 작성한 쿼리를 재사용할 수 있고 명확한 결과를 생성하는 기술을 선택해야 함.