---
layout: post
title:  "JOIN"
parent: Database
grand_parent: School
nav_order: 2
date:   2022-02-11 10:41:00 +0900
---
# 테이블 조인
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## INNER JOIN
---
두 개의 테이블 $A, B$이 있을 때, 각 테이블에서 같은 key가 존재하는 행만 추출

예 - 수상과 대통령이 모두 존재하는 국가

```sql
SELECT p1.country, p1.continent, 
        prime_minister, president
FROM prime_ministers AS p1
INNER JOIN presidents AS p2
ON p1.country = p2.country;

-- 컬럼 이름이 같을 경우에는 `USING` keyword를 사용 가능
SELECT *
FROM left_table
INNER JOIN right_table
USING (id);
```

OUTPUT

| country   | continent| prime_minister     | president|
|---|---|---|---|
| Egypt| Africa| Sherif Ismail| Abdel Fattah el-Sisi|
| Portugal| Europe| Antonio Costa| Marcelo Rebelo de Sousa |
| Vietnam| Asia| Nguyen Xuan Phuc| Tran Dai Quang|
| Haiti| North America | Jack Guy Lafontant | Jovenel Moise|

## SELF JOIN
---
예 - 같은 대륙인 나라끼리 쌍 만들기 (같은 나라끼리는 제외)

```sql
SELECT p1.country, p2.country, p1.continent
FROM prime_ministers AS p1
INNER JOIN prime_ministers AS p2
ON p1.continent = p2.continent AND p1.country <> p2.country
```

OUTPUT

| country1   | country2   | continent   |
|------------|------------|-------------|
| Portugal   | Spain      | Europe      |
| Portugal   | Norway     | Europe      |
| Vietnam    | Oman       | Asia        |
| Vietnam    | Brunei     | Asia        |
| Vietnam    | India      | Asia        |
| India      | Oman       | Asia        |
| India      | Brunei     | Asia        |
| India      | Vietnam    | Asia        |
| Norway     | Spain      | Europe      |
| Norway     | Portugal   | Europe      |
| Brunei     | Oman       | Asia        |
| Brunei     | India      | Asia        |
| Brunei     | Vietnam    | Asia        |

## OUTER JOIN
---
### LEFT JOIN
왼쪽 및 오른쪽 테이블 $A, B$가 있을 때, $A$를 보존하되 $A$와 같은 ID를 갖는 $B$의 행을 JOIN하고 나머지 $A$ 행에 대해서는 $B$의 컬럼에 대해 `NULL` 처리.

```sql
-- 수상 테이블 (p1) 행은 보존하면서 대통령 테이블 (p2)에 없는 나라의 경우는 NULL 처리
SELECT p1.country, prime_minister, president
FROM prime_ministers AS p1
LEFT JOIN presidents AS p2
ON p1.country = p2.country;
```

OUTPUT

| country   | prime_minister | president|
|---|---|---|
| Egypt     | Sherif Ismail | Abdel Fattah el-Sisi    |
| Portugal  | Antonio Costa| Marcelo Rebelo de Sousa |
| Vietnam | Nguyen Xuan Phuc | Tran Dai Quang          |
| Haiti | Jack Guy Lafontant | Jovenel Moise           |
| India | Narendra Modi||
| Australia | Malcolm Turnbull||
| Norway | Erna Solberg ||
| Brunei |Hassanal Bolkiah||
| Oman |Qaboos bin Said al Said||
| Spain |Mariano Rajoy||

### RIGHT JOIN
왼쪽 및 오른쪽 테이블 $A, B$가 있을 때, $B$를 보존하되 $B$와 같은 ID를 갖는 $A$의 행을 JOIN하고 나머지 $B$ 행에 대해서는 $A$의 컬럼에 대해 `NULL` 처리.
- LEFT JOIN과 유사

### FULL JOIN
왼쪽 및 오른쪽 테이블 $A, B$가 있을 때, $A, B$를 모두 보존하되 같은 ID를 갖는 행끼리는 JOIN하고 나머지 행에 대해서는 `NULL` 처리.

```sql
SELECT p1.country AS pm_co, p2.country AS pres_co,
    prime_minister, president
FROM prime_ministers AS p1
FULL JOIN presidents AS p2
ON p1.country = p2.country;
```

OUTPUT

|pm_co| pres_co| prime_minister| president|
|---|---|---|---|
| Egypt| Egypt | Sherif Ismail| Abdel Fattah el-Sisi|
| Portugal| Portugal  | Antonio Costa| Marcelo Rebelo de Sousa |
| Vietnam | Vietnam | Nguyen Xuan Phuc| Tran Dai Quang |
| Haiti | Haiti | Jack Guy Lafontant| Jovenel Moise|
| India || Narendra Modi |
| Australia || Malcolm Turnbull|
| Norway || Erna Solberg|
| Brunei || Hassanal Bolkiah|
| Oman || Qaboos bin Said al Said |                        
| Spain || Mariano Rajoy|
|| Uruguay || Jose Mujica             |
|| Chile || Michelle Bachelet       |
|| Liberia || Ellen Johnson Sirleaf   |

## CROSS JOIN
---
왼쪽 및 오른쪽 테이블 $A, B$에서 발생할 수 있는 모든 combination을 출력

```sql
SELECT prime_minister, president
FROM prime_ministers AS p1
CROSS JOIN presidents AS p2
WHERE p1.continent IN ('North America', 'Oceania');
```

OUTPUT

| prime_minister     | president               |
|--------------------|-------------------------|
| Jack Guy Lafontant | Abdel Fattah el-Sisi    |
| Malcolm Turnbull   | Abdel Fattah el-Sisi    |
| Jack Guy Lafontant | Marcelo Rebelo de Sousa |
| Malcolm Turnbull   | Marcelo Rebelo de Sousa |
| Jack Guy Lafontant | Jovenel Moise           |
| Malcolm Turnbull   | Jovenel Moise           |
| Jack Guy Lafontant | Jose Mujica             |
| Malcolm Turnbull   | Jose Mujica             |
| Jack Guy Lafontant | Ellen Johnson Sirleaf   |
| Malcolm Turnbull   | Ellen Johnson Sirleaf   |
| Jack Guy Lafontant | Michelle Bachelet       |
| Malcolm Turnbull   | Michelle Bachelet       |
| Jack Guy Lafontant | Tran Dai Quang          |
| Malcolm Turnbull   | Tran Dai Quang          |
 