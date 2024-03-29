---
layout: post
title:  "선형 자료구조"
parent: Coding
nav_order: 1
permalink: /docs/coding/linear-ds
date:   2022-04-07 11:59:50 +0900
---
# 책 - 파이썬 알고리즘 인터뷰
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Introduction
---

왜 알고리즘 문제를 푸는가? 수학과 알고리즘을 공부하는 이유는? 왜 이렇게 풀어야 하는가?

튼튼한 기본 `수학`을 바탕으로 논리적 사고 `수학적 사고`를 거쳐 문제 해결 `프로그래밍`을 하기 위해서.

알고리즘에 깃든 다양한 사고 방법, 자료구조, 문제풀이 역량 등은 체계적으로 생각하는 방법을 길러주고 개발자로서 갖춰야 할 지적 기반을 쌓아준다.

테스트 주도 개발 (TDD, Test-driven development): 가급적 테스트를 많이 진행하면서 일부러라도 버그를 유발해 문제를 수정해 나가는 형태

제네릭 (Generic): 파라미터 타입이 나중에 지정 (to-be-specified-later)되게 해서 재활용성을 높일 수 있는 프로그래밍 스타일

구조체 (Struct): 메모리의 어느 영역에나, 어떤 크기로든 할당할 수 있는 복합 자료형
- 배열의 경우 순차적으로 메모리 할당

리스트 컴프리헨션 (List Comprehension): 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문

제너레이터 (Generator): 루프의 Iteration 동작을 제어할 수 있는 루틴 형태

알고리즘은 시간 `Time Complexity`과 공간 `Space Complexity`의 Trade-off

분할 상환 분석 (Amortized Analysis): 최악의 경우를 여러 번에 걸쳐 골고루 나눠주는 형태로 계산된 시간 복잡도

## 문자열 조작 (Ch6)
---
[유효한 팰린드롬, Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- 문자열
    - `string.isalpha()`: string이 alphabet으로 구성되었는지 (ASCII Code 기준) check 
    - `string.isnumeric()`: string이 numeric으로 구성되었는지 (ASCII Code 기준) check
    - `string.isalnum()`: string이 alphanumeric (alphabet OR numeric)인지 (ASCII Code 기준) check
    - **모든 문자를 일일이 점검한다**
- 정규식
    - `re.sub('[^a-z0-9]', "", string)`: `string`에서 alphanumeric을 제외한 모든 character를 제거한다
        - `^`: NOT (제외한다)
        - `a-z`: lower-case alphabet
        - `0-9`: number
    - **문자열 전체를 한번에 처리한다**
- C는 컴파일 언어: 원시코드를 기계어 변환 `Build` 후 런타임에서 기계어 코드 실행
- Python은 인터프리터 언어: `Build`없이 런타임에서 한 줄 씩 실행

[문자열 뒤집기, Reverse String](https://leetcode.com/problems/reverse-string)
- 투 포인터 (Two pointer): 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식

[로그 파일 재정렬, Reorder Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)
- `string.isdigit()`
- 람다 표현식 (Lambda Expression): 식별자 (Identifier) 없이 실행 가능한 함수
    - `list.sort(key = lambda x: (A, B, ...))`
        - `A`: 정렬 우선순위 1
        - `B`: (`A`로 정렬했을 때 같은 순서인 경우) 정렬 우선순위 2

[가장 흔한 단어, Most Common Word](https://leetcode.com/problems/most-common-word)
- `re.sub('[^\w]', " ", string)`
    - `\w`: word character = `[A-Za-z0-9_]`

[그룹 애너그램, Group Anagrams](https://leetcode.com/problems/group-anagrams)
- In-place sort: 입력을 출력으로 덮어쓰는, 별도 추가 공간이 필요하지 않은 정렬 방식
- Timsort

[가장 긴 팰린드롬 부분 문자열, Longest Palindrome Substring](https://leetcode.com/problems/longest-palindrome-substring)
- **아이디어**: 홀수의 경우와 짝수의 경우에 대하여 Two pointer를 활용
- 문자 표현 방식
    1. ASCII (1Byte)
    2. Unicode (2-4Bytes)
    3. UTF-8 (가변 길이 문자 인코딩 방식)

## 배열 (Ch7)
---
자료구조
- Continuous (연속, 메모리 공간 기반)
- Link (연결, 포인터 기반)
    - 포인터: 메모리 영역을 1바이트 단위로 가리키는 주소

배열: 크기를 지정하고, 해당 크기만큼의 **연속된 메모리 공간**을 할당받는 작업을 수행하는 자료형
- $O(1)$에 **검색**이 가능하다

동적 배열: 크기를 지정하지 않고 자동으로 리사이징하는 배열
- `ArrayList (JAVA), std::vector (C++), list (Python)`
- 미리 초깃값을 작게 잡아 배열을 생성한 뒤 데이터가 추가되면서 Full되었을 떄, 늘려주고 모두 복사
    - 새로운 배열을 할당하고 기존 데이터를 옮겨야 하므로 $O(n)$의 비용 발생
        - 분할 상환 분석에 의한 삽입 $O(1)$
        - Growth factor (재할당 비율)

[두 수의 합, Two Sum](https://leetcode.com/problems/two-sum)
- **아이디어**: Target에서 요소를 뺀 나머지 값의 존재여부를 확인한다

[빗물 트래핑, Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)
- **아이디어**: 막대는 높낮이에 무관하게, 전체 부피에 영향을 끼치지 않고 왼쪽/오른쪽을 가르는 장벽 역할
    - Two pointer를 이용하는 방법
    - Stack을 이용하는 방법

[세 수의 합, 3Sum](https://leetcode.com/problems/3sum)
- **아이디어**: 정렬 후 요소를 기준으로 오른쪽 서브 배열에 대한 Two pointer 검색

[배열 파티션 1, Array Partition 1](https://leetcode.com/problems/array-partition-i)
- Pair의 min-value 합을 최대로

[자신을 제외한 배열의 곱, Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)
- 나눗셈을 사용하지 않고 $O(n)$에 풀이하기
- **아이디어**: 자신을 기준으로 왼쪽의 결과, 오른쪽의 결과를 곱한다

[주식을 사고팔기 가장 좋은 시점, Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
- 기술 통계학 (Descriptive Statistics): 값을 시각화하여 문제 풀이의 직관을 얻는 방식

## 연결 리스트 (Ch8)
---
연결 리스트: 데이터 요소의 선형 집합으로, 데이터 순서가 메모리에 물리적 순서대로 저장되진 않는다
- 데이터를 **구조체**로 묶어서 **포인터**로 연결한다
- 탐색에는 $O(n)$ (특정 인덱스에 접근하기 위해 전체를 순서대로 읽어야 한다)
- Head나 Tail에서 삭제 및 추가, 추출에는 $O(1)

[팰린드롬 연결 리스트, Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list)
- 런너 (Runner): 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법
    - Fast runner: 전체 길이를 알기 위해 2칸씩 전진
    - Slow runner: 전체 길이의 중간 지점을 알기 위해 1칸씩 전진
- 다중 할당 (Multiple Assignment)

[두 정렬 리스트의 병합, Merge Two Sorted Lists](https://leetcode.com/problems/palindrome-linked-list)
- **아이디어**: 작은 값의 위치를 고정한다, Recursion - Backtracking

[역순 연결 리스트, Reverse Linked List](https://leetcode.com/problems/reverse-linked-list)
- Iteration 방식과 **Recursion 방식**

[두 수의 덧셈, Add Two Numbers](https://leetcode.com/problems/add-two-numbers)
- `functools`: Higher-Order function (고계 함수, 함수를 다루는 함수)를 지원하는 함수형 언어 모듈
    - `functools.reduce`: 두 Argument의 함수를 누적 적용하라는 메소드

[노드 스왑](https://leetcode.com/problems/swap-nodes-in-pairs)
- Iteration 방식과 **Recursion 방식**

[홀짝 연결 리스트](https://leetcode.com/problems/odd-even-linked-list)
- **아이디어**: 홀수 번째의 연결 리스트와 짝수 번째의 연결 리스트를 잇는다.

[역순 연결 리스트 2](https://leetcode.com/problems/reverse-linked-list-ii)

## 스택, 큐 (Ch9)
---
콜 스택 (Call stack): 컴퓨터 프로그램의 서브루틴에 대한 정보를 저장하는 자료구조

[유효한 괄호](https://leetcode.com/problems/valid-parentheses)
- `char in dictionary`: char가 dictionary의 **key**로 존재하는지 확인
- Mapping Table을 작성한다

[중복 문자 제거](https://leetcode.com/problems/remove-duplicate-letters)
- **아이디어**: 문자간 순서를 고려하고, 등장한 문자가 이후에도 등장하는가
- Recursion 방식
    - 전체 집합과 접미사 집합이 같다 = 접두사 집합은 결국 접미사에서도 나타난다
- List (Stack), Set, Counter을 활용한 방식
    - Counter: 현재 나온 문자가 그 이후에도 나올 것인지 Check
    - List: 쌓여있는 문자와 현재 문자의 순서를 비교하며, 현재 문자가 빠른 순서면 List에서 제거

[일일 온도](https://leetcode.com/problems/daily-temperatures)

큐 (Queue)는 Deque, Priority Queue로 변형되었으며, BFS (Breadth-First Search)나 캐시 등을 구현할 때 사용됨

[큐를 이용한 스택 구현](https://leetcode.com/problems/implement-stack-using-queues)
- 큐에 넣어있는 걸 빼서 다시 넣으면 LIFO가 가능하다

[스택을 이용한 큐 구현](https://leetcode.com/problems/implement-queue-using-stacks)
- 두 개의 스택 A, B를 이용해서 A에 있는 것을 B에 넣으면 FIFO가 가능하다

[원형 큐 디자인](https://leetcode.com/problems/design-circular-queue)
- Ring Buffer (기존의 큐와 동일하나, 마지막 위치가 시작 위치와 연결된다)
    - 기존의 큐는 앞쪽 요소들이 모두 빠져서 충분한 공간이 있음에도 그쪽으로 추가할 수 없었다
    - 동작 방식은 Two pointer와 비슷하다 (front and rear)
    - `%` (modulo 연산)

## 데크, 우선순위 큐 (Ch10)
---
데크 (Deque, Double-ended Queue)는 양쪽에서 삭제와 삽입을 모두 처리할 수 있으며 스택과 큐의 특징을 모두 가지고 있다

[원형 데크 디자인](https://leetcode.com/problems/design-circular-deque)
- head와 tail이 dummy node이다

우선순위 큐 (Priority Queue)는 특정 조건에 따라 우선순위가 가장 높은 요소가 추출되는 자료형
- 다익스트라 알고리즘에 활용된다
- `PriorityQueue` 모듈: Thread-safe를 제공하며, Locking Overhead가 발생할 수 있다
- heap과 관련이 깊다: `heapq` 모듈
    - Python은 최소 힙 (Min-heap)만 지원한다

Python이 느린 이유: 전역 인터프리터 락 (GIL, Global Interpreter Lock)
- Python 객체에 대한 접근을 제한하여 동시성 관리를 편리하게 하고 메모리 관리를 쉽게 하고자 함
- 하나의 스레드가 자원을 독점하는 형태로 실행됨

[k개 정렬 리스트 병합](https://leetcode.com/problems/merge-k-sorted-lists)
- **아이디어**: 최소 값을 갖는 노드만 뽑아내자

## 해시 테이블 (Ch11)
---
HashMap, Hash Table은 key를 value에 mapping할 수 있는 구조
- 대부분의 연산이 (분활 상환 분석에 따른) 시간 복잡도가 $O(1)$

Hash function: 임의 크기를 갖는 데이터를 고정 크기 값으로 mapping하는데 사용할 수 있는 함수
- Hash table을 Indexing하기 위해 hash function을 사용한다 = hashing
    - 정보를 가능한 한 빠르게 저장 및 검색하기 위해 사용
- 체크섬 (checksum), 손실 압축 (lossy compression), 무작위화 함수 (Randomization Function) 등에 사용

Load factor: Hash table에 저장된 데이터 수 $n$을 bucket의 수 $k$로 나눈 것, $\frac{n}{k}$
- hash function을 재작성할지 아니면 hash table의 크기를 조정할 지 결정
- Load factor가 증가할수록 hash table의 성능은 점점 감소

개별 체이닝 (Separate Chaining): 충돌 발생 시 연결 리스트로 Link하는 방식
- Red-black Tree (자가 균형 이진 탐색 트리)

오픈 어드레싱 (Open Addressing): 충돌 발생 시 탐사를 통해 빈 공간을 찾는 방식
- 모든 원소가 반드시 자신의 hash value와 일치하는 주소에 저장되는 보장이 없다
- 선형 탐사 (Linear Probing)
    - 충돌 발생 시 해당 위치부터 순차적으로 탐사를 진행
    - 단점: Clustering 발생 시 탐사 시간이 오래 걸리고 hashing 효율이 감소
- 데이터 수가 bucket size보다 큰 경우에는 삽입할 수 없다: $n>k$
    - Load factor 값을 넘어서게 되면 Growth factor에 따라 Rehashing이 일어난다

[해시맵 디자인](https://leetcode.com/problems/design-hashmap)
- `defaultdict`에서 존재하지 않는 index로 조회를 시도할 경우, Error를 발생시키지 않고 그 자리에서 바로 Default 객체를 생성한다

[보석과 돌](https://leetcode.com/problems/jewels-and-stones)

[중복 문자 없는 가장 긴 부분 문자열](https://leetcode.com/problems/longest-substring-without-repeating-characters)
- **아이디어**: Sliding window, Two pointer

[상위 k 빈도 요소](https://leetcode.com/problems/top-k-frequent-elements)
- Heap 삽입 방식
    1. `list`에 모두 삽입한 다음 마지막에 `heapify()`
    2. 매번 `heappush()`를 하는 방식

`zip()`: 2개 이상의 시퀀스를 **짧은 길이**를 기준으로 일대일 대응하는 새로운 tuple 시퀀스를 만드는 역할
- 여러 시퀀스에서 동일한 index의 item을 순서대로 추출하여 tuple로 묶어주는 역할
- generator에서 실젯값을 추출하려면 `list()`로 묶는다

`*` (Asterisk): 시퀀스 언패킹 연산자 (Sequence Unpacking Operator)
- 주로 tuple이나 list를 풀어헤치는데 사용한다
- 함수의 parameter가 되었을 때는 패킹 (Packing)도 가능하다
- 변수의 할당도 묶어서 처리할 수 있다.

`**`: key/value 페어를 Unpacking하는데 사용한다.


