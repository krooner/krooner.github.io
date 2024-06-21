---
layout: post
title:  "Set Theory"
parent: SQL
grand_parent: 'School (2013-2022)'
date:   2022-02-14 10:41:00 +0900
last_modified_date: 2024-06-21
---
# 집합 연산
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## UNION and UNION ALL

```sql
-- UNION 중복되는 행 **미포함**
-- 국가의 모든 수상과 군주를 추출 (수상과 군주가 동일 사람이면 한번만)
SELECT prime_minister AS leader, country
FROM prime_ministers
UNION
SELECT monarch, country
FROM monarchs
ORDER BY country;
```

|leader | country   |
|---|---|
| Malcolm Turnbull | Australia |
| Hassanal Bolkiah | Brunei    | 
| Sherif Ismail | Egypt     |
| Jack Guy Lafontant | Haiti     |
| Narendra Modi | India     |
| Harald V | Norway    |
| Erna Solberg | Norway    |
| Qaboos bin Said al Said | Oman      |

```sql
-- UNION ALL 중복되는 행 **포함**
-- 국가의 모든 수상과 군주 (수상과 군주가 동일 사람이어도 출력)
SELECT prime_minister AS leader, country
FROM prime_ministers
UNION ALL
SELECT monarch, country
FROM monarchs
ORDER BY country;
```

| leader | country   |
|---|---|
| Malcolm Turnbull | Australia |
| Hassanal Bolkiah | Brunei    |
| Hassanal Bolkiah | Brunei    |
| Sherif Ismail | Egypt     |
| Jack Guy Lafontant | Egypt     |
| Narendra Modi | India     |
| Erna Solberg | Norway    |
| Harald V | Norway    |
| Qaboos bin Said al Said | Oman      |
| Qaboos bin Said al Said | Oman   |

## INTERSECT

```sql
-- 수상과 대통령이 모두 있는 나라
SELECT country
FROM prime_ministers
INTERSECT
SELECT country
FROM presidents;
```

|country|
|---|
|Portugal|
|Vietnam|
|Haiti|
|Egypt|

```sql
-- 나라의 수상과 대통령이 같은 사람인 경우
SELECT country, prime_minister AS leader
FROM prime_ministers
INTERSECT
SELECT country, president
FROM presidents;
```

|country|leader|
|---|---|
|||

## EXCEPT

```sql
-- 나라의 수상은 아닌 군주
SELECT monarch, country
FROM monarchs
EXCEPT
SELECT prime_minister, country
FROM prime_ministers;
```

|monarch|country|
|---|---|
|Harald V|Norway|
|Felipe VI|Spain|

## Semi-joins and Anti-joins

```sql
-- Semi-join 
-- "독립을 1800년 이전에 한 나라"의 대통령, 나라, 대륙명
SELECT president, country, continent
FROM presidents
WHERE country IN
    (SELECT name
     FROM states
     WHERE indep_year < 1800);
```

|president|country|continent|
|---|---|---|
|Marcelo Rebelo de Sousa|Portugal|Europe|

```sql
-- Anti-join
-- 'America'로 끝나는 대륙에 있으면서 "1800년 이전에 독립한 나라가 아닌" 나라의 대통령, 나라, 대륙명
SELECT president, country, continent
FROM presidents
WHERE continent LIKE '%America'
    AND country NOT IN
        (SELECT name
         FROM states
         WHERE indep_year < 1800);
```

| president         | country   | continent     |
|-------------------|-----------|---------------|
| Jovenel Moise     | Haiti | North America |
| Jose Mujica       | Uruguay | South America |
| Michelle Bachelet | Chile | South America |