---
layout: post
title:  "Window Function"
parent: SQL
grand_parent: 'School (2013-2022)'
date:   2022-02-15 16:52:00 +0900
last_modified_date: 2024-06-21
---
# 윈도우 함수
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

```sql
-- 집계 함수 값 (aggregate values)을 추출할 때, 
-- 모든 non-aggregate columns (country_id, season, date)에 대해 `GROUP BY`를 적용하도록 요구된다.
SELECT
  country_id, season, date,
  AVG(home_goal) AS avg_home
FROM match
GROUP BY country_id;
-- ERROR: column "match.season" must appear in the GROUP BY clause or be used in an aggregate function
```

## Window Functions

윈도우 함수는 현재 행 (Current row) 와 연관된 행 집합 (Window) 에 대해 계산을 수행한다.
- `GROUP BY` 집계 함수와 유사하지만, 윈도우 함수의 경우 **모든 행이 OUTPUT에 남아있다**.
- Aggregate calculation은 `SELECT` 문에서의 서브쿼리와 유사함.
- (`ORDER BY` 문을 제외하고) 모든 쿼리가 처리된 이후에 수행되며 쿼리 결과를 활용함
- PostgreSQL, Oracle, MySQL, SQL Server 등에서는 지원하지만, SQLite에서는 지원하지 않음

```sql
FUNCTION_NAME() OVER(...)
-- ORDER BY
-- PARTITION BY
-- ROWS/RANGE PRECEDING/FOLLOWING/UNBOUNDED
```

> 윈도우 함수의 활용
> 1. 이전 또는 이후 행들로부터 값들을 Fetch: 현재 챔피언이 누구인지 (Reigning champion), 시간에 따른 성장 계산 (Growth over time)
> 2. 정렬된 리스트 내 값의 위치를 기반으로 각 행의 랭킹을 매김
> 3. 누계 (Running total)와 이동 평균 (Moving average) 계산

## ORDER BY

`OVER` 안에 `ORDER BY`를 적용하면, 현재 행과 연관된 행들이 정렬된다.

```sql
-- 최근 연도 순으로 번호 붙이기
SELECT
  Year, Event, Country,
  ROW_NUMBER() OVER (ORDER BY Year DESC) AS ROW_N
FROM Summer_Medals WHERE Medal = 'Gold';
```

| Year | Event         | Country | Row_N |
|------|---------------|---------|-------|
| 2012 | Wg 96 KG|IRI|1|
| 2012 | 4X100M Medley|USA|2|
| 2012 | Wg 84 KG|RUS|3|
| ... | ...|...|...|
| 2008 | 50M Freestyle | BRA |637|
|2008|96-120KG |CUB |638|
| ... | ... | ...|...|

```sql
-- 최근 연도-종목 이름 순으로 번호 붙이기
SELECT
  Year, Event, Country,
  ROW_NUMBER() OVER
    (ORDER BY Year DESC, Event ASC) AS Row_N
FROM Summer_Medals WHERE Medal = 'Gold';
```

| Year | Event | Country | Row_N | 
|------|---------|---------|-------| 
|2012|+100KG|FRA |1 | 
|2012|+67KG|SRB |2 | 
|2012|+78KG |CUB |3 | 
|... |... |... |... |

```sql
-- 최근 연도-종목 이름 순으로 번호 붙이고, 국가명-순번 순으로 정렬
-- ORDER BY in/out OVER: `OVER` 문 안에 있는 `ORDER BY`가 적용된 다음, 밖에 있는 `ORDER BY`가 적용된다.
SELECT
  Year, Event, Country,
  ROW_NUMBER() OVER
    (ORDER BY Year DESC, Event ASC) AS Row_N
FROM Summer_Medals WHERE Medal = 'Gold' ORDER BY Country ASC, Row_N ASC;
```

| Year | Event   | Country | Row_N |
|------|---------|---------|-------|
| 2012 | 1500M|ALG|36| 
| 2000 | 1500M|ALG |1998| 
| 1996 | 1500M|ALG |2662| 
| ...  | ...|... |... |

## PARTITION BY

컬럼 내 고유 값을 기반으로 테이블을 여러 개의 partitions으로 분리하며, 같은 컬럼 내에서도 다른 계산을 수행한다.
- 1개 이상의 컬럼에 대하여 데이터를 partition할 수 있다.
- aggregate calculation, ranks에 대해서도 수행할 수 있다.
- 윈도우 함수에 의해 각각 처리된다
  - `ROW_NUMBER`는 각 partition마다 초기화 된다.
  - `LAG`는 이전 행이 같은 partition에 있을 때만 이전 값을 fetch한다.


```sql
-- 종목-연도별 전년도 챔피언
WITH Discus_Gold AS (...)

SELECT
  Year, Event, Champion,
  LAG(Champion) OVER
    (PARTITION BY Event
     ORDER BY Event ASC, Year ASC) AS Last_Champion
FROM Discus_Gold
ORDER BY Event ASC, Year ASC;
```

|Year |Event |Champion |Last_Champion |
|---|---|---|---|
| 2004 | Discus Throw | LTU| null          |
| 2008 | Discus Throw | EST| LTU          |
| 2012 | Discus Throw | GER| EST           |
| 2004 | Triple Jump  | SWE| null          |
| 2008 | Triple Jump  | POR| SWE           |
| 2012 | Triple Jump  | USA| POR           |

```sql
-- 경기별 득점 수 및 해당 국가 리그-시즌 평균 득점 수와 비교
SELECT
  c.name,
  m.season,
  (home_goal + away_goal) AS goals,
  AVG(home_goal + away_goal)
      OVER(PARTITION BY m.season, c.name) AS season_ctry_avg
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
```

| name        | season    | goals     | season_ctry_avg |
|-------------|-----------|-----------|-----------------|
| Belgium     | 2011/2012 | 1| 2.88            |
| Netherlands | 2014/2015 | 1| 3.08            |
| Belgium     | 2011/2012 | 1| 2.88            |
| Spain       | 2014/2015 | 2| 2.66            |

## Fetching

### LAG (Relative)

`LAG(column, n) OVER (...)`
- 현재 행으로부터 `n`개의 행 **이전**에 있는 `column`의 값을 반환
- `LAG(column, 1) OVER (...)`은 이전 행에 있는 `column`의 값

```sql
-- Reigning champion: 올해와 작년 대회 모두 우승한 챔피언
-- 서로 다른 두 개의 컬럼에 작년 챔피언과 올해 챔피언이 현재 행에 같이 있음
-- `올해 우승자 (A) / 작년 우승자 (A)`
WITH Discus_Gold AS (
  SELECT
    Year, Country AS Champion
  FROM Summer_Medals
  WHERE
    Year IN (1996, 2000, 2004, 2008, 2012)
    AND Gender = 'Men' AND Medal = 'Gold'
    AND Event = 'Discus Throw')
SELECT
  Year, Champion,
  LAG(Champion, 1) OVER
    (ORDER BY Year ASC) AS Last_Champion
FROM Discus_Gold
ORDER BY Year ASC;
```

| Year | Champion | Last_Champion |
|------|----------|---------------|
|1996|GER | null          |
|2000|LTU | GER           |
|2004|LTU| LTU           |
|2008|EST| LTU           |
|2012|GER| EST           |

### LEAD (Relative)
`LEAD(column, n) OVER (...)` 현재 행으로부터 `n`개의 행 **이후**에 있는 `column`의 값을 반환

```sql
-- 올림픽 개최 연도, 도시, 차기 도시, 차차기 도시
WITH Hosts AS (
  SELECT DISTINCT Year, City
  FROM Summer_Medals)

SELECT
  Year, City,
  LEAD(City, 1) OVER (ORDER BY Year ASC)
    AS Next_City,
  LEAD(City, 2) OVER (ORDER BY Year ASC)
    AS After_Next_City
FROM Hosts
ORDER BY Year ASC;
```

| Year | City      | Next_City | After_Next_City |
|------|-----------|-----------|-----------------|
| 1896 | Athens| Paris     | St Louis        |
| 1900 | Paris| St Louis  | London          |
| 1904 | St Louis| London| Stockholm       |
| 1908 | London| Stockholm| Antwerp         |
| 1912 | Stockholm| Antwerp| Paris           |
| ...  | ...| ...| ...             |

### FIRST_VALUE, LAST_VALUE (Absolute)

`FIRST_VALUE(column)`는 테이블 또는 파티션 내 첫번째 값을 반환하며 `LAST_VALUE(column)`는 테이블 또는 파티션 내 마지막 값을 반환

```sql
-- 올림픽 개최 연도, 도시, 최초 도시, 최근 도시
-- 기본적으로 (By default), 윈도우는 테이블 첫 행부터 시작해서 현재 행에서 종료된다.
-- `RANGE BETWEEN ...` 문은 윈도우를 테이블 또는 파티션의 끝까지 확장시킬 수 있다.
SELECT
  Year, City,
  FIRST_VALUE(City) OVER
    (ORDER BY Year ASC) AS First_City,
  LAST_VALUE(City) OVER (
   ORDER BY Year ASC
   RANGE BETWEEN
     UNBOUNDED PRECEDING AND
     UNBOUNDED FOLLOWING
  ) AS Last_City
FROM Hosts
ORDER BY Year ASC;
```

| Year | City      | First_City | Last_City       |
|------|-----------|------------|-----------------|
| 1896 | Athens| Athens| London          |
| 1900 | Paris| Athens| London          |
| 1904 | St Louis| Athens| London          |
| 1908 | London| Athens| London          |
| 1912 | Stockholm| Athens| London          |

## Ranking

|방식|설명|
|---|---|
|`ROW_NUMBER`| 두 행의 값이 일치하더라도 항상 고유 숫자를 부여한다|
|`RANK`| 같은 값을 갖는 행에 대해서는 같은 값을 부여하고, 다음 숫자는 건너뛴다 (skipping over): `1st - 2nd - 2nd - 4th`|
|`DENSE_RANK`| 같은 값을 갖는 행에 대해서는 같은 값을 부여하고, 다음 숫자를 건너뛰지 않는다: `1st - 2nd - 2nd - 3rd`|

```sql
-- 국가별 올림픽 참가 횟수 순위
WITH Country_Games AS (
  SELECT
    Country, COUNT(DISTINCT Year) AS Games
  FROM Summer_Medals
  WHERE
    Country IN ('GBR', 'DEN', 'FRA',
                'ITA', 'AUT', 'BEL',
                'NOR', 'POL', 'ESP')
  GROUP BY Country
  ORDER BY Games DESC)

SELECT
  Country, Games,
  ROW_NUMBER()
    OVER (ORDER BY Games DESC) AS Row_N,
  RANK()
    OVER (ORDER BY Games DESC) AS Rank_N,
  DENSE_RANK()
    OVER (ORDER BY Games DESC) AS Dense_Rank_N
FROM Country_Games
ORDER BY Games DESC, Country ASC;
```

| Country | Games | Row_N |Rank_N|Dense_Rank_N|
|---------|-------|-------|---|---|
| GBR |27 |1 |1|1|
| DEN  |26 |2 |2|2|
| FRA  |26 |3 |2|2|
| ITA |25 |4 |4|3|
| AUT |24 |5 |5|4|
| BEL |24 |6 |5|5|
|NOR  |22 |7 | 7|5|
|POL |20 |8 | 8|6|
|ESP|18 |9 |9|7|

> `ROW_NUMBER`와 `RANK`는 마지막 RANK가 행의 수 (9)로 동일하나, `DENSE_RANK`의 마지막 랭크는 랭크에 쓰인 고유값의 갯수이다.

## Paging

데이터를 (거의) 동일한 사이즈의 청크들로 분할하는 것으로, 많은 API들은 전송할 데이터를 줄이기 위해서 **페이지** 형태로 데이터를 반환한다. 성능 평가를 위해 데이터를 4분위 (Quartile) 또는 3분위 (Thirds, 상위-중간-하위 33%)로 분할

### NTILE

`NTILE(n)`은 데이터를 `n`개의 (거의) 동일한 페이지들로 분할한다.

```sql
-- 메달 수를 기준으로 국가를 3분위로 분할
WITH Country_Medals AS (
  SELECT
    Country, COUNT(*) AS Medals
  FROM Summer_Medals
  GROUP BY Country),

SELECT
  Country, Medals,
  NTILE(3) OVER (ORDER BY Medals DESC) AS Third
FROM Country_Medals;
```

| Country | Medals | Third |
|---------|--------|-------|
| USA | 4585|1 |
| URS| 2049|1 |
| GBR| 1720|1 |
|... |... |... | 
| CZE|56 |2 |
| LTU|55|2 |
| ...|... |... | 
| DOM |6|3 |
|BWI |5|3 |
|...|... |... | 

```sql
-- 분위별 국가 평균 메달 수
WITH Country_Medals AS (...),
Thirds AS (
SELECT
    Country, Medals,
    NTILE(3) OVER (ORDER BY Medals DESC) AS Third
  FROM Country_Medals)

SELECT
Third,
  ROUND(AVG(Medals), 2) AS Avg_Medals
FROM Thirds
GROUP BY Third
ORDER BY Third ASC;
```

|Third|Avg_Medals|
|---|---|
|1|598.74|
|2|22.98|
|3|2.08|

## Aggregate (Function)

```sql
-- 연도별 메달 수, 해당 연도까지 메달 최대 갯수와 합계
WITH Brazil_Medals AS (
  SELECT
    Year, COUNT(*) AS Medals
  FROM Summer_Medals
  WHERE
    Country = 'BRA'
    AND Medal = 'Gold'
    AND Year >= 1992
  GROUP BY Year
  ORDER BY Year ASC)

SELECT
  Year, Medals,
  MAX(Medals)
    OVER (ORDER BY Year ASC) AS Max_Medals,
  SUM(Medals) OVER (ORDER BY Year ASC) AS Medals_RT
FROM Brazil_Medals;
```

| Year | Medals | Max_Medals |
|------|--------|------------|
| 1992 | 13|13|13|
| 1996 | 5|13|18|
| 2004 | 18|18|36|
| 2008 | 14|18|50|
| 2012 | 14|18|64|

```sql
-- 2011/12 시즌 경기별 골 수와 평균 골 수
SELECT
    date,
    (home_goal + away_goal) AS goals,
    AVG(home_goal + away_goal) OVER() AS overall_avg
FROM match
WHERE season = '2011/2012';
```

| date       | goals | overall_avg       |
|------------|-------|-------------------|
 | 2011-07-29 | 3| 2.71646           |
| 2011-07-30 | 2| 2.71646           |
| 2011-07-30 | 4| 2.71646           |
| 2011-07-30 | 1| 2.71646           |

## Frames

Frame: `RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`
- Frame을 적용하지 않으면 `LAST_VALUE`는 City 컬럼에서 현재 행의 값을 리턴할 것이다
- 기본적으로 (By default) Frame은 테이블 또는 파티션의 시작부터 현재 행까지 설정되기 때문이다.

```sql
LAST_VALUE(City) OVER (
 ORDER BY Year ASC
 RANGE BETWEEN
   UNBOUNDED PRECEDING AND
   UNBOUNDED FOLLOWING
) AS Last_City
```

### ROWS BETWEEN

`ROWS BETWEEN [START] AND [FINISH]`
- `n PRECEDING`: 현재 행으로부터 이전 `n` 행
- `CURRENT ROW`: 현재 행
- `n FOLLOWING`: 현재 행으로부터 이후 `n` 행
- `UNBOUNDED PRECEDING`: 테이블/파티션의 맨 처음
- `UNBOUNDED FOLLOWING`: 테이블/파티션의 맨 마지막

|예시|설명|
|---|---|
|`ROWS BETWEEN 3 PRECEDING AND CURRENT ROW`|현재 이전 3번째 행 (C-3)부터 현재 행 (C)까지 총 4개의 행|
|`ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING`|현재 이전 3번째 행 (C-1)부터 현재 다음 행 (C+1)까지 총 3개의 행|
|`ROWS BETWEEN 5 PRECEDING AND 1 PRECEDING`|현재 이전 5번째 행 (C-5)부터 현재 이전 행 (C-1)까지 총 5개의 행|


```sql
-- 러시아의 연도별 메달 수, 이전까지 최대 메달, 전년도 중 많은 메달
WITH Russia_Medals AS (
  SELECT
  Year, COUNT(*) AS Medals
  FROM Summer_Medals
  WHERE
    Country = 'RUS'
    AND Medal = 'Gold'
  GROUP BY Year
  ORDER BY Year ASC;
)

SELECT
  Year, Medals,
  MAX(Medals)
    OVER (ORDER BY Year ASC) AS Max_Medals,
  MAX(Medals)
    OVER (ORDER BY Year ASC
          ROWS BETWEEN
          1 PRECEDING AND CURRENT ROW)
    AS Max_Medals_Last
  MAX(Medals)
    OVER (ORDER BY Year ASC
          ROWS BETWEEN
          CURRENT ROW AND 1 FOLLOWING)
    AS Max_Medals_Next
FROM Russia_Medals
ORDER BY Year ASC;
```

| Year | Medals | Max_Medals | Max_Medals_Last |Max_Medals_Next|
|---|---|---|---|---|
|1996|36 |36 |36 |66|
|2000|66 |66 |66 |66|
|2004|47 |66 |66 |47|
|2008|43 |66 |47 |47|
|2012|47 |66 |47 |47|

## Moving Averages and Totals

Moving average는 이전 `n` 기간 동안의 평균 (지난 10일 동안의 평균 판매량)
- 모멘텀/트렌드를 나타내는데 사용되며, Seasonality을 제거하는데 유용하다
- 특정한 기간마다 어떤 패턴을 가지고 반복하는지 확인할 수 있는 특성

Moving total는 이전 `n` 기간 동안의 합계 (지난 3번의 올림픽 메달 수 총합)
- 성능을 나타내는데 사용되며, 합계가 감소하면 전체 성능 또한 감소한다


```sql
-- 1980년 이후 올림픽에서 미국 금메달
WITH US_Medals AS (SELECT
  Year, COUNT(*) AS Medals
FROM Summer_Medals
WHERE
  Country = 'USA'
  AND Medal = 'Gold'
  AND Year >= 1980
GROUP BY Year
ORDER BY Year ASC)

SELECT
  Year, Medals,
  AVG(Medals) OVER
    (ORDER BY Year ASC
     ROWS BETWEEN
     2 PRECEDING AND CURRENT ROW) AS Medals_MA
  SUM(Medals) OVER
    (ORDER BY Year ASC
     ROWS BETWEEN
     2 PRECEDING AND CURRENT ROW) AS Medals_MT
FROM US_Medals
ORDER BY Year ASC;
```

| Year | Medals | Medals_MA |Medals_MT|
|------|--------|-----------|---|
|1984|168 | 168.00    |168|
| 1988 | 77| 122.50    |245|
| 1992 | 89| 111.33    |334|
|1996|160 | 108.67    |326|
|2000|130| 126.33    |379|
|2004|116| 135.33    |406|
|2008|125| 123.67    |371|
|2012|147| 129.33    |388|

## ROWS and RANGE

`RANGE BETWEEN [START] AND [FINISH]`
- `ROWS BETWEEN`과 유사하지만, `RANGE`는 `OVER(ORDER BY ...)` 문에서 발생하는 duplicates를 하나의 entity로 간주한다.
- 사실상 `ROWS BETWEEN`만 항상 활용된다고 보면 된다.

| Year | Medals | Rows_RT | Range_RT |
|------|--------|---------|----------|
|1992|10|10|10|
|1996|50|60|110|
|2000|50|110|110|
|2004|60|170|230|
|2008|60|230|230|
|2012|70|300|300|