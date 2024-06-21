---
layout: post
title:  "Common Datatype"
parent: SQL
grand_parent: 'School (2013-2022)'
date:   2022-02-17 15:19:00 +0900
last_modified_date: 2024-06-21
---
# 공통 데이터 타입
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
SELECT title, description, special_features FROM FILM LIMIT 5
```

|title|description|special_features|
|---|---|---|
| ACADEMY D...  | A Epic...| {Deleted Scenes,Behi...}|
| ACE GOLD...   | A Astound..|{Trailers, Deleted Scenes}|
| AFFAIR PR...  | A Fanciful,..|{Commentaries,Behind the...}|


```sql
-- 테이블의 데이터 타입 찾기
SELECT column_name, data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE column_name in ('title','description','special_features') AND table_name ='film';
```

| column_name      | data_type         |
|------------------|-------------------|
| title            | character varying |
| description      | text              |
| special_features | ARRAY             |

## 텍스트 `CHAR`, `VARCHAR`, `TEXT`

```sql
-- `CONCAT` 함수 활용하여 문자열 연결
SELECT CONCAT(first_name,' ', last_name) AS full_name FROM customer;
```

| first_name | last_name | full_name         |
|------------|-----------|-------------------|
| MARY       | SMITH     | MARY SMITH        |
| LINDA      | WILLIAMS  | LINDA WILLIAMS    |


```sql
-- `||` 연산자 (non-string input도 가능) 활용하여 문자열 연결
SELECT customer_id || ': ' || first_name || ' ' || last_name AS full_name FROM customer;
```

| full_name         |
|-------------------|
| 1: MARY SMITH     |
| 2: LINDA WILLIAMS |

```sql
-- 대문자 및 소문자 변환
SELECT UPPER(title) AS UP, LOWER(title) AS LO, INITCAP(title) AS IC FROM film;
-- 대문자, 소문자, 단어 첫 글자만
```

|UP|LO|IC|
|---|---|---|
|ACADEMY DINOSAUR|academy dinosaur|Academy Dinosaur|
|ACE GOLDFINGER|ace goldfinger|Ace Goldfinger|
|ADAPTATION HOLES|adaptation holes|Adaptation Holes|

```sql
-- 문자열 대체
SELECT REPLACE(description, 'A Astounding', 'An Astounding') as description FROM film;
    -- 타겟 컬럼, 원래 substring, 변경된 substring
```

|description|
|---|
|A Epic Drama of a Feminist And a Mad Scientist...       |
|An Astounding Epistle of a Database Administrator...    |
|An Astounding Reflection of a Lumberjack And a Car...   |

```sql
-- 문자열 뒤집기
SELECT title, REVERSE(title) FROM film AS f;
```

| title            | reverse(title)   |
|------------------|------------------|
| ACADEMY DINOSAUR | RUASONID YMEDACA |
| ACE GOLDFINGER   | REGNIFDLOG ECA   |

```sql
-- 문자열 길이
SELECT title, CHAR_LENGTH(title) FROM film;
    -- LENGTH(title)와 동일
```

| title             | CHAR_LENGTH(title)  |
|-------------------|---------------------|
| ACADEMY DINOSAUR  | 16                  |
| ACE GOLDFINGER    | 14                  |
| ADAPTATION HOLES  | 16                  |



```sql
-- 문자열 내 문자의 위치 찾기
SELECT email, POSITION('@' IN email) AS IDX FROM customer;
    -- STRPOS(email, '@')와 동일
```

| email | IDX |
|---|---|
| MARY.SMITH@sakilacustomer.org| 11|
| PATRICIA.JOHNSON@sakilacustomer.org | 17|
| LINDA.WILLIAMS@sakilacustomer.org | 15|

```sql
-- 문자열 파싱
SELECT LEFT(description, 50) FROM film; -- 첫 50개 문자 추출
SELECT RIGHT(description, 50) FROM film; -- 마지막 50개 문자 추출
```

```sql
-- 문자열 내 Substring 추출

-- 10번째 위치 문자부터 50개 문자 (Substring) 추출
SELECT SUBSTRING(description, 10, 50) FROM film AS f;
    -- SUBSTR(description, 10, 50)과 동일

-- 처음 문자부터 @ 문자 이전까지 Substring 추출
SELECT SUBSTRING(email FROM 0 FOR POSITION('@' IN email)) FROM customer;

-- @ 다음 문자부터 끝 문자까지 Substring 추출
SELECT SUBSTRING(email FROM POSITION('@' IN email)+1 FOR CHAR_LENGTH(email)) FROM customer;
```

문자열 공백 제거하기

`TRIM([leading | trailing | both] [characters] FROM string)`
1. 첫번째 파라미터 (LEFT, RIGHT, BOTH-SIDE)
2. 두번째 파라미터 (제거할 문자)
3. 세번째 파라미터 (타겟 문자열)

```sql
SELECT 
    TRIM('  padded  '),
-- 'padded'
    LTRIM('  padded   '),
-- 'padded   '
    RTRIM('  padded   '),
-- '  padded'
    LPAD('padded', 10, '#'),
-- '####padded'
    LPAD('padded', 10)
-- '    padded'
    LPAD('padded', 5)
-- '    padde'
    RPAD('padded', 10, '#')
-- 'padded####'
```

## 숫자 (`INT`, `DECIMAL`)

날짜/시간 (`TIMESTAMP`, `DATE`, `TIME`, `INTERVAL`)
- `TIMESTAMP`: `2019-03-26 01:05:17.93027+00`. ISO 8601 (yyyy-mm-dd) 형식을 따른다
- `DATE`: `2005-05-28`
- `TIME`: `01:05:17.93027+00`
- `INTERVAL`: `rental_date`가 `2005-05-24 22:53:30`

```sql
SELECT rental_date + INTERVAL '3 days' as expected_return FROM rental;
```

|expected_return|
|---|
|2005-05-27 22:53:30|

```sql
SELECT timestamp '2019-05-01' + 21 * INTERVAL '1 day';
```

|timestamp without timezone|
|---|
|2019-05-22 00:00:00|

```sql
-- 산술 연산 (Arithmetic Operation)
SELECT 
    date '2005-09-11' - date '2005-09-10' AS INT1,
    date '2005-09-11' + integer '3' AS DATE2;
```

|INT1|DATE2|
|---|---|
|1|2005-09-14|



```sql
-- `AGE()`
-- 다음 두 쿼리는 동일한 결과 출력
SELECT date '2005-09-11 00:00:00' - date '2005-09-09 12:00:00';
SELECT AGE(timestamp '2005-09-11 00:00:00', timestamp '2005-09-09 12:00:00');
```

|interval|
|---|
|1 day 12:00:00|

```sql
-- `NOW()`
SELECT NOW();
```

|now()|
|---|
|2019-04-19 02:51:18.448641+00|

```sql
-- Casting
-- PostgreSQL specific casting
SELECT NOW()::timestamp;

-- CAST() function
SELECT CAST(NOW() as timestamp);

-- 결과는 동일
-- 2019-04-19 02:51:18.448641
```



```sql
-- `CURRENT_TIMESTAMP`
SELECT CURRENT_TIMESTAMP AS CT1,
    CURRENT_TIMESTAMP(2) AS CT2;
```

|CT1|CT2|
|---|---|
|2019-04-19 02:51:18.448641+00|2019-04-19 02:51:18.44+00|



```sql
-- `CURRENT_DATE, CURRENT_TIME`
SELECT CURRENT_DATE, CURRENT_TIME;
```

|current_date|current_time|
|---|---|
|2019-04-19|04:06:30.929845+00:00|

## 추출 및 변형 (Extracting and Transforming)

`EXTRACT(), DATE_PART(), DATE_TRUNC()` 함수
- 시간의 정확도가 크게 중요하지 않을 때 `2005-05-13 08:53:53`
- Timestamp의 일부만 추출하면 될 때 `2005 or 5 or 2 or Friday`
- 표준화를 위해 Timestamp를 변환하거나 잘라야할 때 `2005-05-13 00:00:00`

```sql
-- `EXTRACT (field FROM source)`, `DATE_PART ('field', source)`
SELECT EXTRACT(quarter FROM timestamp '2005-01-24 05:12:00') AS quarter;
SELECT DATE_PART('quarter', timestamp '2005-01-24 05:12:00') AS quarter;
```

|quarter|
|---|
|1|

```sql
-- DVD 렌탈 비용 테이블에서 연도별, 분기별 지불 금액
SELECT
  EXTRACT(quarter FROM payment_date) AS quarter,
  EXTRACT(year FROM payment_date) AS year,
  SUM(amount) AS total_payments
FROM payment GROUP BY 1, 2;
```

| quarter | year | total_payments | 
|---------|------|----------------|
| 2 | 2005 | 14456.31 |
| 3 | 2005 | 52446.02 |
| 1 | 2006 | 514.18 |

```sql
-- `DATE_TRUNC`: timestamp 또는 interval 데이터 타입을 truncate
SELECT DATE_TRUNC('year', TIMESTAMP '2005-05-21 15:30:30') AS T1,
DATE_TRUNC('month', TIMESTAMP '2005-05-21 15:30:30') AS T2;
```

|T1|T2|
|---|---|
|2005-01-01 00:00:00|2005-05-01 00:00:00|

## ARRAY

```sql
-- 테이블 생성 
CREATE TABLE my_first_table (first_column text, second_column integer);

-- 행 삽입
INSERT INTO my_first_table (first_column, second_column) VALUES ('text value', 12);

-- 두 개의 array 컬럼을 갖는 테이블
CREATE TABLE grades (student_id int, email text[][], test_scores int[] );

-- backslash 필요없음 (jekyll error 때문에 붙인거임)
INSERT INTO grades
    VALUES (1,
    '\{\{"work","work1@datacamp.com"\},\{"other","other1@datacamp.com"\}\}',
    '\{92,85,96,88\}' );
```

### ACCESS and SEARCH

> __PostgreSQL array의 index는 1부터 시작합니다__

```sql
SELECT email[1][1] AS type, email[1][2] AS address, test_scores[1] FROM grades WHERE email[1][1] = 'work';
```

| type   |  address           | test_scores |
|--------|--------------------|-------------|
| work   | work1@datacamp.com | 92          |
| work   | work2@datacamp.com | 76          |

## ANY
```sql
SELECT email[2][1] as type, email[2][2] as address, test_scores[1] FROM grades WHERE 'other' = ANY (email);
-- 다음 WHERE문과 동일함; WHERE email @> ARRAY['other'];
```

| type | address | test_scores |
|---|---|---| 
| other | other1@datacamp.com | 92 |
|null |null |76 |  