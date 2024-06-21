---
layout: post
title:  "Basic"
parent: SQL
grand_parent: 'School (2013-2022)'
date:   2022-02-11 09:19:00 +0900
nav_order: 1
last_modified_date: 2024-06-21
---
# 기본 문법
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## SELECT
```sql
SELECT * FROM table_name -- 테이블 내 전체 컬럼 선택하기
SELECT column_name FROM table_name -- 단일 컬럼 선택하기
SELECT column_name1, column_name2, ... FROM table_name -- 다수 컬럼 선택하기
```

## DISTINCT, LIMIT
```sql
SELECT DISTINCT column_name FROM table_name -- 컬럼 내 고유값 선택하기 (DISTINCT)
SELECT * FROM table_name LIMIT 5 -- 테이블 내 첫 5개 행만 출력하기
```

## WHERE

```sql
SELECT * FROM table_name WHERE column_name > 10 -- 컬럼 값이 10보다 큰/작은 행 (>, <)
SELECT * FROM table_name WHERE column_name = 'apple' -- 컬럼 값이 apple 인/아닌 행 (=, !=)
SELECT * FROM table_name WHERE column_name = '2022-01-01' -- 2022년 1월 1일에 해당하는 행 (ISO date format)
SELECT * FROM table_name WHERE column_name > 10 AND column_name < 10 -- 컬럼 값이 10과 20 사이인 행 (AND)
SELECT * FROM table_name WHERE column_name BETWEEN 10 AND 20 -- 더 쉽게 (BETWEEN)

SELECT * FROM table_name WHERE column_name = 10 OR column_name = 15 OR column_name = 20
-- 컬럼 값이 10 또는 15 또는 20인 행 (OR)
SELECT * FROM table_name WHERE column_name IN (10, 15, 20)-- 더 쉽게 (IN)


SELECT * FROM table_name WHERE column_name IS NULL -- 컬럼 값이 비어있는 행 (IS NULL, IS NOT NULL)
```

### Wildcard
컬럼 값의 패턴 찾기 (wildcard를 활용한 LIKE, NOT LIKE)

```sql
-- `%` (텍스트 내 0개 이상의 문자와 매칭)
-- A로 시작하는 컬럼 값이 있는 행 ('A%')
SELECT * FROM table_name WHERE column_name LIKE 'A%' 

-- `_` (단일 문자와 매칭)
-- 두 번째 문자가 B인 컬럼 값이 있는 행 ('_B%')
SELECT * FROM table_name
WHERE column_name LIKE '_B%'
```

## 집계 함수 (Aggregating functions)

COUNT, SUM, AVG, MAX, MIN

```sql
SELECT COUNT(*) FROM table_name -- 테이블 행 갯수 구하기 (COUNT)
SELECT SUM(column_name) FROM table_name -- 컬럼 값의 총합
SELECT SUM(column_name2) FROM table_name WHERE column_name1 > 10 -- 컬럼1 값이 10 보다 큰 행들의 컬럼2 값 총합
```

### Aliasing (AS)

테이블이나 컬럼, 결과값에 임시 이름을 붙이는 것

```sql
SELECT (column_name / 10) AS division FROM table_name -- 컬럼 값을 10으로 나눈 몫
```

## ORDER BY

```sql
SELECT * FROM table_name ORDER BY column_name -- default는 오름차순 (텍스트의 경우 알파벳 순)
SELECT * FROM table_name ORDER BY column_name DESC -- 컬럼 값을 기준 내림차순 정렬 (텍스트의 경우 알파벳 역순)

-- 컬럼1과 컬럼2 값을 기준으로 오름차순 정렬
-- 우선순위: 컬럼1 > 컬럼2 (컬럼1 값이 같을 때, 컬럼2를 기준으로 순서 정함)
SELECT * FROM table_name ORDER BY column_name1, column_name2
```

## GROUP BY

영화 정보를 담은 테이블 (films)의 컬럼: 영화 제목 (title), 개봉 연도 (release_year), 제작 국가 (country), 제작 비용 (budget), 순이익 (gross)

```sql
-- 각 연도마다 개봉한 영화의 수
SELECT release_year, COUNT(*) FROM films GROUP BY release_year

-- 각 연도-국가별 개봉 영화 중 최대 제작 비용
SELECT release_year, country, MAX(budget) FROM films GROUP BY release_year, country
```

## HAVING

**집계 함수는 WHERE문에서 사용할 수 없다**

```sql
-- 개봉된 영화 수가 10개보다 많은 연도
SELECT release_year FROM films GROUP BY release_year WHERE COUNT(title) > 10 -- ERROR!

-- 이럴 때는 이렇게
SELECT release_year FROM films GROUP BY release_year HAVING COUNT(title) > 10
```

## CASE WHEN


```sql
-- CASE 문 구조
CASE WHEN <condition1> THEN <result1>
    WHEN <condition2> THEN <result2>
    ...
    ELSE <result_else> END AS new_column

-- 매치 테이블에서 홈팀 득점과 어웨이팀 득점, 그리고 두 득점에 따른 outcome을 CASE문을 활용하여 추출
SELECT id,
  home_goal,
  away_goal,
  CASE WHEN home_goal > away_goal THEN 'Home Team Win'
       WHEN home_goal < away_goal THEN 'Away Team Win'
       ELSE 'Tie' END AS outcome
FROM match
WHERE season = '2013/2014';
```

|id|home_goal|away_goal|outcome|
|---|---|---|---|
|1237|2 |0 |Home Team Win| 
|1238|0 |1 |Away Team Win| 
|1239|1 |0 |Home Team Win| 
|1240|0 |0 |Tie |

```sql
-- 첼시 (team_id = 8455) 경기 날짜, 시즌, 첼시의 승리 여부
SELECT date, season,
  CASE WHEN hometeam_id = 8455 AND home_goal > away_goal
            THEN 'Chelsea home win!'
       WHEN awayteam_id = 8455 AND home_goal < away_goal
            THEN 'Chelsea away win!' END AS outcome
FROM match
WHERE CASE WHEN hometeam_id = 8455 AND home_goal > away_goal
                THEN 'Chelsea home win!'
           WHEN awayteam_id = 8455 AND home_goal < away_goal
                THEN 'Chelsea away win!' END 
      IS NOT NULL;
-- WHERE 문을 추가해서 NULL인 경우 (무승부/패배 경기) 제외
```

| date       | season    | outcome           |
|------------|-----------|-------------------|
| 2011-11-05 | 2011/2012 | Chelsea away win! |
| 2011-11-26 | 2011/2012 | Chelsea home win! |
| 2011-12-03 | 2011/2012 | Chelsea away win! |

```sql
-- 리버풀 (team_id = 8650)의 시즌별 홈 승리와 원정 승리 수
-- COUNT이기 때문에 THEN 다음 결과 값이 크게 중요하지 않다
SELECT
    season,
    COUNT(CASE WHEN hometeam_id = 8650 AND home_goal > away_goal
          THEN 54321 END) AS home_wins,
    COUNT(CASE WHEN awayteam_id = 8650 AND away_goal > home_goal
          THEN 'Some random text' END) AS away_wins
FROM match
GROUP BY season;
```

| season    | home_wins | away_wins |
|-----------|-----------|-----------|
| 2011/2012 | 6 |8|
| 2012/2013 | 9|7|
| 2013/2014 | 16|10|
| 2014/2015 | 10|8|

```sql
-- 리버풀의 시즌별 홈 경기 득점과 원정 경기 득점
SELECT
    season,
    SUM(CASE WHEN hometeam_id = 8650
          THEN home_goal END) AS home_goals,
    SUM(CASE WHEN awayteam_id = 8650
          THEN away_goal END) AS away_goals
FROM match
GROUP BY season;
```

|season|home_goals|away_goals|
|---|---|---|
 | 2011/2012 | 24|23 |
| 2012/2013 | 33 |38 |
| 2013/2014 | 53 |48 |
| 2014/2015 | 30|22 |

```sql
-- 첼시의 홈 승리 확률 및 원정 승리 확률 (무승부 제외)
SELECT
  season,
  ROUND(AVG(CASE WHEN hometeam_id = 8455 AND home_goal > away_goal THEN 1
           WHEN hometeam_id = 8455 AND home_goal < away_goal THEN 0
           END),2) AS pct_homewins,
  ROUND(AVG(CASE WHEN awayteam_id = 8455 AND away_goal > home_goal THEN 1
           WHEN awayteam_id = 8455 AND away_goal < home_goal THEN 0
           END),2) AS pct_awaywins
FROM match
GROUP BY season;
```

| season    | pct_homewins     | pct_awaywins     |
|-----------|------------------|------------------|
| 2011/2012 | 0.75|0.5 | 
| 2012/2013 | 0.86|0.67 | 
| 2013/2014 | 0.94|0.67 | 
| 2014/2015 | 1|0.79 |