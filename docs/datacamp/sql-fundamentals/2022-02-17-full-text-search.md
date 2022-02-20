---
layout: post
title:  "Full-text Search"
parent: SQL Fundamentals
grand_parent: DataCamp
nav_order: 10
date:   2022-02-17 22:52:00 +0900
---
# Full-text Search
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## LIKE 연산자
---
`Case-sensitive`하다.
- `_` wildcard: 정확히 한 문자에 매칭될 때 사용
- `%` wildcard: 0개 이상의 문자에 매칭될 때 사용

```sql
SELECT title
FROM film
WHERE title LIKE 'ELF%';
-- ELF PARTY

SELECT title
FROM film
WHERE title LIKE '%ELF';
-- ENCINO ELF

SELECT title
FROM film
WHERE title LIKE '%elf%';
-- EMPTY..
```

## Full-text Search
---
DB내 텍스트 데이터에 대한 자연언어 (natural language) 쿼리를 수행하기 위한 수단을 제공한다
- Stemming (어간 추출)
- Spelling mistakes (오탈자)
- Ranking

```sql
SELECT title, description
FROM film
WHERE to_tsvector(title) @@ to_tsquery('elf');
```

`to_tsvector(text)`는 `text`에서 관사 (a/an, the)나 어미 (-ful) 등을 제거하고, 명사와 동사만을 추출함
- (INPUT) A Fateful Display of a Womanizer And a Mad Scientist who must Outgun a A Shark in Soviet Georgia
- (OUTPUT) 'display':3 'fate':2 'georgia':19 'mad':9 'must':12 'outgun':13 'scientist':10 'shark':16 'soviet':18 'woman':6

OUTPUT

| title                |
|----------------------|
| ELF PARTY            |
| ENCINO ELF           |
| GHOSTBUSTERS ELF     |

## 사용자 정의 데이터 타입
열거형 (Enumerated) 데이터 타입

```sql
CREATE TYPE dayofweek AS ENUM (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
);
```

```sql
SELECT typname, typcategory
FROM pg_type
WHERE typname='dayofweek';
```

OUTPUT

| typname   | typcategory |
|-----------|-------------|
| dayofweek | E           |

```sql
SELECT column_name, data_type, udt_name
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name ='film';
```

OUTPUT

| column_name | data_type| udt_name|
|---|---|---|
| title| character varying | varchar|
| rating| USER-DEFINED| mpaa_rating |

## 사용자 정의 함수
```sql
CREATE FUNCTION squared(i integer) RETURNS integer AS $$
    BEGIN
        RETURN i * i;
    END;
$$ LANGUAGE plpgsql;

SELECT squared(10);
-- 100
```

## PostgreSQL Extensions
---
주로 사용되는 Extensions
- PostGIS
- PostPic
- fuzzystrmatch
    - `SELECT levenshtein('GUMBO', 'GAMBOL')`
    - 2 (U  $\rightarrow$ A 변경, L 추가)
- pg_trgm
    - `SELECT similarity('GUMBO', 'GAMBOL')`
    - 0.18181818

### 사용가능한 Extension
```sql
SELECT name FROM pg_available_extensions;
```

OUTPUT

|name | 
|---| 
| dblink | 
| pg_stat_statements |

### 설치된 Extension
```sql
SELECT extname FROM pg_extension;
```

OUTPUT

|name|
|---|
|plpgsql|

### Extension 추가
```sql
--Enable the fuzzystrmatch extension
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
--Confirm that fuzzstrmatch has been enabled
SELECT extname FROM pg_extension;
```

OUTPUT

|name|
|---|
|plpgsql|
|fuzzystrmatch|