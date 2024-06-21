---
layout: post
title:  "Full-text Search"
parent: SQL
grand_parent: 'School (2013-2022)'
date:   2022-02-17 22:52:00 +0900
last_modified_date: 2024-06-21
---
# 전체 텍스트 검색
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## LIKE 연산자

`Case-sensitive`하며 `_` wildcard는 정확히 한 문자에 매칭될 때 사용하고 `%` wildcard는 0개 이상의 문자에 매칭될 때 사용한다.

```sql
SELECT title FROM film WHERE title LIKE 'ELF%'; -- ELF PARTY
SELECT title FROM film WHERE title LIKE '%ELF'; -- ENCINO ELF
SELECT title FROM film WHERE title LIKE '%elf%'; -- EMPTY..
```

## Full-text Search

DB에 있는 텍스트 데이터에 대한 자연언어 (natural language) 쿼리를 수행하기 위한 수단을 제공한다: Stemming (어간 추출), Spelling mistakes (오탈자), Ranking

```sql
-- `to_tsvector(text)`는 `text`에서 관사 (a/an, the)나 어미 (-ful) 등을 제거하고, 명사와 동사만을 추출함
SELECT title, description FROM film WHERE to_tsvector(title) @@ to_tsquery('elf');

-- (INPUT) A Fateful Display of a Womanizer And a Mad Scientist who must Outgun a A Shark in Soviet Georgia
-- (OUTPUT) 'display':3 'fate':2 'georgia':19 'mad':9 'must':12 'outgun':13 'scientist':10 'shark':16 'soviet':18 'woman':6
```

| title                |
|----------------------|
| ELF PARTY            |
| ENCINO ELF           |
| GHOSTBUSTERS ELF     |

## 사용자 정의 데이터 타입

```sql
-- 열거형 (Enumerated) 데이터 타입
CREATE TYPE dayofweek AS ENUM (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
);

SELECT typname, typcategory FROM pg_type WHERE typname='dayofweek';
```

| typname   | typcategory |
|-----------|-------------|
| dayofweek | E           |

```sql
SELECT column_name, data_type, udt_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name ='film';
```

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

SELECT squared(10); -- 100
```

## PostgreSQL Extensions

주로 사용되는 Extensions으로는 PostGIS, PostPic 등이 있다.

```sql
SELECT name FROM pg_available_extensions;
```

|name | 
|---| 
| dblink | 
| pg_stat_statements |

```sql
SELECT extname FROM pg_extension;
```

|name|
|---|
|plpgsql|

```sql
-- Enable the fuzzystrmatch extension
-- fuzzystrmatch `SELECT levenshtein('GUMBO', 'GAMBOL')`
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;

-- Confirm that fuzzstrmatch has been enabled
-- pg_trgm `SELECT similarity('GUMBO', 'GAMBOL')`
SELECT extname FROM pg_extension;
```

|name|
|---|
|plpgsql|
|fuzzystrmatch|