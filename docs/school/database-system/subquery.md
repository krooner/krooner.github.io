---
layout: post
title:  "Subqueries"
parent: Database
grand_parent: School
nav_order: 5
date:   2022-02-14 16:12:00 +0900
---
# 서브 쿼리
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 서브쿼리
---
또 다른 쿼리 안에 `중첩된 쿼리`로, 중간 단계에서의 Data Transformation에 활용된다.
- 쿼리 내 임의의 단계에 포함될 수 있다: `SELECT, FROM, WHERE, GROUP BY`
- 다양한 정보를 반환할 수 있다: `스칼라 값, 리스트, 테이블`
- 컴퓨팅 파워를 요구하므로, DB 및 액세스하는 테이블의 크기를 고려해야 함

서브쿼리의 역할
1. 요약된 값으로 그룹을 비교한다
> EPL 팀들의 연 평균 성적과 리버풀의 성적을 비교
2. 데이터를 재구성한다 (Reshape)
> 분데스리가에서 월 평균 최대 득점은 몇 골인가
3. JOIN 연산을 할 수 없는 데이터를 결합한다
> 경기 결과 테이블에서 홈 팀과 어웨이 팀의 이름을 추출

```sql
SELECT column
FROM (SELECT column
      FROM table) AS subquery;
```

## WHERE 문 내 서브쿼리
---
예 - 폴란드 리그에 있는 팀

```sql
-- 폴란드 (국가 ID = 15722), team 테이블과 match 테이블을 사용
SELECT
  team_long_name,
  team_short_name AS abbr
FROM team
WHERE
  team_api_id IN
  (SELECT hometeam_id
   FROM match
   WHERE country_id = 15722);
```

OUTPUT

|team_long_name|abbr|
|---|---|
| Ruch Chorzów|CHO|
| Jagiellonia|BIA| 
| Lech Pozna?|POZ| 
| P. Warszawa|PWA| 
| Cracovia |CKR|
| Górnik ??czna | LEC |
| Polonia Bytom | GOR |
| Zag??bie Lubin | ZAG |
| Pogo? Szczecin | POG | 
| Widzew ?ód? |WID|
| ?l?sk Wroc?aw | SLA |

예 - 전 세계 출산율 평균 이하인 아시아 국가 이름과 출산율

```sql
SELECT name, fert_rate
FROM states
WHERE continent = 'Asia'
    AND fert_rate <
        (SELECT AVG(fert_rate)
         FROM states);
```

OUTPUT

|name|fert_rate|
|---|---|
|Brunei|1.96|
|Vietnam|1.7|

## SELECT 문 내 서브쿼리
---
단일 값 (Single value)를 리턴하며 개별 값들과 비교하기 위해 집계 함수 값을 포함한다. (Otherwise, ERROR!)
- 적절한 위치에 필터링을 수행했는지 체크해야 함
    - 메인 쿼리와 서브 쿼리를 둘 다 필터링
- 수학적 계산에 활용된다: 평균과의 편차 (Deviation)

예 - 2011/2012 시즌 경기별 득점 수와 평균 득점과의 차이

```sql
SELECT
  date,
  (home_goal + away_goal) AS goals,
  (home_goal + away_goal) -
     (SELECT AVG(home_goal + away_goal)
      FROM match
      WHERE season = '2011/2012') AS diff
FROM match
WHERE season = '2011/2012';
```

OUTPUT

| date       | goals | diff              |
|------------|-------|-------------------|
| 2011-07-29 | 3| 0.28354037267081  |
| 2011-07-30 | 2| -0.71645962732919 |
| 2011-07-30 | 4| 1.28354037267081  |
| 2011-07-30 | 1| -1.71645962732919 |

예 - 대륙별 수상 보유 국가의 수

```sql
SELECT DISTINCT continent,
    (SELECT COUNT(*)
     FROM states
     WHERE prime_ministers.continent = states.continent) AS countries_num
FROM prime_ministers;
```

OUTPUT

|continent|countries_num|
|---|---|
|Africa|2|
|Asia|4|
|Europe|3|
|North America|1|
|Oceania|1|

## FROM 문 내 서브쿼리
---
데이터를 사전 필터링 하거나 `SELECT` 이전에 데이터를 변형하며, 하나의 `FROM` 문에 여러 서브쿼리를 만들 수 있다
- Alias (AS) 별칭 처리하기
- JOIN 조인


예 - 2011/2012 시즌 홈 평균 득점 TOP 3 팀 구하기
- `Aggregates of aggregates`: 홈 평균 득점 TOP 3 팀 구하기
  1. 각 팀의 `AVG`를 계산
  2. Highest 값을 갖는 TOP 3 팀을 구함

```sql
SELECT team, home_avg
FROM (SELECT
          t.team_long_name AS team,
          AVG(m.home_goal) AS home_avg
      FROM match AS m
      LEFT JOIN team AS t
      ON m.hometeam_id = t.team_api_id
      WHERE season = '2011/2012'
      GROUP BY team) AS subquery
ORDER BY home_avg DESC
LIMIT 3;
```

OUTPUT

|team|home_avg|
|---|---|
| FC Barcelona   | 3.8421   |
| Real Madrid CF | 3.6842   |
| PSV            | 3.3529   | 

예 - 군주가 존재하는 대륙과 대륙국가 중 의회 여성 구성 최대 비율

```sql
SELECT DISTINCT monarchs.continent, subquery.max_perc
FROM monarchs,
    (SELECT continent, MAX(women_parli_perc) AS max_perc
     FROM states
     GROUP BY continent) AS subquery
WHERE monarchs.continent = subquery.continent
ORDER BY continent;
```

OUTPUT

|continent|max_perc|
|---|---|
|Asia|24|
|Europe|39.6|