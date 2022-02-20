---
layout: post
title:  "유용한 함수들"
parent: SQL Fundamentals
grand_parent: DataCamp
nav_order: 8
date:   2022-02-16 19:47:00 +0900
---
# Useful functions
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Pivoting
---
중국, 러시아, 미국의 올림픽 연도별 금메달

```sql
WITH Country_Awards AS (
  SELECT
    Country, Year, COUNT(*) AS Awards
  FROM Summer_Medals
  WHERE
    Country IN ('CHN', 'RUS', 'USA')
    AND Year IN (2004, 2008, 2012)
    AND Medal = 'Gold' AND Sport = 'Gymnastics'
  GROUP BY Country, Year
  ORDER BY Country ASC, Year ASC)

SELECT
  Country, Year,
  RANK() OVER
    (PARTITION BY Year ORDER BY Awards DESC) :: INTEGER
    AS rank
FROM Country_Awards
ORDER BY Country ASC, Year ASC;
```

OUTPUT

| Country | Year |Rank | 
|---------|------|-----| 
|CHN |2004|3 | 
|CHN |2008|1 | 
|CHN |2012|1 | 
|RUS |2004|1 | 
|RUS |2008|2 | 
|RUS |2012|2 | 
|USA |2004|2 | 
|USA |2008|3 | 
|USA |2012|3 |

### CROSSTAB
`Year`를 기준으로 Pivot

```sql
CREATE EXTENSION IF NOT EXISTS tablefunc;

SELECT * FROM CROSSTAB($$
  ... -- 이전 OUTPUT 테이블
$$) AS ct (Country VARCHAR,
           "2004" INTEGER,
           "2008" INTEGER,
           "2012" INTEGER)
ORDER BY Country ASC;
```

OUTPUT

| Country | 2004 | 2008 | 2012 | 
|---------|------|------|------| 
|CHN |3 |1 |1 | 
|RUS |1 |2 |2 | 
|USA |2 |3 |3 |

## ROLLUP and CUBE
---
### ROLLUP
group-level aggregation에 대한 추가적인 row를 포함하는 `GROUP BY` subclause
  - GROUP BY `Country, ROLLUP(Medal)`
    1. `Country & Medal`-level 합계를 계산
    2. `Country`-level 합계만 계산하고 `Medal` 컬럼은 `null`로 대신함

예 - 08 하계 올림픽 중국과 러시아의 메달 별 획득 수

```sql
SELECT
  Country, Medal, COUNT(*) AS Awards
FROM Summer_Medals
WHERE
  Year = 2008 AND Country IN ('CHN', 'RUS')
GROUP BY Country, ROLLUP(Medal)
ORDER BY Country ASC, Medal ASC;
```

OUTPUT

| Country | Medal | Awards | 
|---------|--------|--------| 
|CHN |Bronze|57 | 
|CHN |Gold |74 | 
|CHN |Silver|53 | 
|CHN |Total|184 | 
|RUS |Bronze|56 | 
|RUS |Gold |43 | 
|RUS |Silver|44 |
|RUS |Total|143 |

`ROLLUP`은 hierarchical하며, 가장 왼쪽에 있는 컬럼부터 오른쪽 컬럼까지 de-aggregating
  - `ROLLUP(Country, Medal)`: `Country`-level 합계를 포함
  - `ROLLUP(Medal, Country)`: `Medal`-level 합계를 포함
  - 두 케이스 모두 grand total을 포함

```sql
SELECT
  Country, Medal, COUNT(*) AS Awards
FROM summer_medals
WHERE
  Year = 2008 AND Country IN ('CHN', 'RUS')
GROUP BY ROLLUP(Country, Medal)
ORDER BY Country ASC, Medal ASC;
```

OUTPUT

| Country | Medal | Awards |
|---------|--------|--------| 
|CHN |Bronze|57 |
|CHN |Gold |74 |
|CHN |Silver|53 |
|CHN |null |184 |
|RUS |Bronze|56 |
|RUS |Gold |43 |
|RUS |Silver|44 |
|RUS |null |143 |
|null |null |327 |

1. Group-level total은 모든 level이 `null`인 행
2. `ROLLUP(Country, Medal)`이므로 `Country`-level
  - `Medal`-level도 같이 계산하고 싶다면?

### CUBE
non-hierarchical `ROLLUP`으로, 모든 가능한 group-level aggregation을 생성한다.
- `CUBE(Country, Medal)`은 `Country`-level, `Medal`-level, grand total을 계산한다.

```sql
SELECT
  Country, Medal, COUNT(*) AS Awards
FROM summer_medals
WHERE
  Year = 2008 AND Country IN ('CHN', 'RUS')
GROUP BY CUBE(Country, Medal)
ORDER BY Country ASC, Medal ASC;
```

OUTPUT

| Country | Medal  | Awards |
|---------|--------|--------|
|CHN |Bronze|57 |
|CHN  |Gold |74 |
|CHN |Silver|53 |
|CHN  |null |184 |
|RUS |Bronze|56 |
|RUS |Gold |43 |
|RUS |Silver|44 |
|RUS |null |143 |
| null | Bronze | 113 |
|null |Gold |117 |
|null |Silver|97 |
|null |null |327 |

### ROLLUP vs CUBE
 
예 - 08, 09년 1,2분기 판매량

| Year | Quarter | Sales |
|------|---------|-------| 
|2008|Q1 |12 |
|2008|Q2 |15 |
|2009|Q1 |21 |
|2009|Q2 |27 |

`ROLLUP(Year, Quarter)`
- hierarchical data가 있을 때
- 가능한 모든 group-level aggregation이 필요없을 때

| Year | Quarter | Sales | 
|------|---------|-------|
|2008|null |27 |
|2009|null |48 |
|null|null |75 |

`CUBE(Year, Quarter)`
- 가능한 모든 group-level aggregation이 필요할 때

| Year | Quarter | Sales | 
|------|---------|-------|
|2008|null |27 |
|2009|null |48 |
|null|Q1 |33 |
|null|Q2 |42 |
|null|null |75 |

## Useful Functions
---
### COALESCE
list_of_values를 input으로 받고 첫 번째 non-null value를 output으로 반환
- `COALESCE(null, null, 1, null, 2) => 1`
- `null`을 반환하는 SQL operations에 유용하다
  - `ROLLUP, CUBE`, Pivoting, `LAG, LEAD`

```sql
SELECT
  COALESCE(Country, 'Both countries') AS Country,
  COALESCE(Medal, 'All medals') AS Medal,
  COUNT(*) AS Awards
FROM summer_medals
WHERE
  Year = 2008 AND Country IN ('CHN', 'RUS')
GROUP BY ROLLUP(Country, Medal)
ORDER BY Country ASC, Medal ASC;
```

OUTPUT

| Country        | Medal      | Awards |
|----------------|------------|--------|
 | Both countries| All medals| 327 |
| CHN| All medals | 184 |
| CHN| Bronze |57 | 
| CHN| Gold|74 | 
| CHN| Silver|53 | 
| RUS| All medals| 143 | 
| RUS| Bronze|56 | 
| RUS| Gold|43 | 
| RUS| Silver|44 |

### STRING_AGG
`STRING_AGG(column, separator)`는`column` 내 모든 값들을 받아서 값 사이에 `separator`를 넣어서 concatenate함

```sql
WITH Country_Medals AS (...),
  Country_Ranks AS (...)
  SELECT STRING_AGG(Country, ', ')
  FROM Country_Medals;
```

OUTPUT: `CHN, RUS, USA`
