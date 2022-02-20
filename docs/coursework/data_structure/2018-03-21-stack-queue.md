---
title: "스택과 큐"
layout: post
parent: Data Structures
grand_parent: Coursework
nav_order: 3
date:   2018-03-21 14:30:00 +0900
---
# Stacks
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 스택 (Stacks)
---
삽입과 제거가 LIFO (Last-in first-out) 방식을 따른다.
- 주요 기능
    - $push(object)$: 요소 삽입
    - $pop()$: 가장 마지막에 삽입된 요소를 제거한다.
- 보조 기능
    - $top()$: 가장 마지막에 삽입된 요소를 반환한다. (제거 X)
    - $size()$: 저장된 요소의 수를 반환한다.
    - $empty()$: 저장된 요소들이 존재하는지 여부를 반환한다.
- 예시
    - 웹 브라우저에서 페이지 방문 기록
    - 텍스트 편집기에서 실행 취소 기능
    - 다른 자료구조의 컴포넌트 
    - 괄호 매칭 (Parentheses Matching)

### 배열 기반 스택
- 왼쪽에서 오른쪽으로 요소를 추가
- $top$ 요소의 인덱스를 저장하는 변수 사용
```python
def size():
    return t + 1
def empty():
    return t < 0
def top():
    if empty():
        raise StackEmpty
    return S[t]
def push(e):
    if size() == N:
        raise StackFull
    t = t + 1
    s[t] = e
def pop():
    if empty():
        raise StackEmpty
    t = t - 1
```

### 성능 및 한계
스택에 $n$개의 요소가 있을 때 공간복잡도는 $O(n)$이며, 각 기능은 $O(1)$의 시간복잡도를 갖는다.

스택의 최대 크기는 사전에 정의되어 변경될 수 없고, 꽉찬 스택에 새로운 요소를 추가하는 것은 `배열 기반의 스택`에서는 Exception이 발생한다.

### Span 계산하기
![stack_1](../../../assets/images/2018-03-21-image-1.png){: width="250" }

배열 $X$가 주어졌을 때, $X[i]$의 span $S[i]$는 X[j] 직전 (immediately preceding) 에 있는 요소들 중 $X[j]\leq X[i]$를 만족하는 최대 연속 요소 수이다.
- $S[0] = 1$: 자기 자신 ($X[0]$)
- $S[1] = 1$: 자기 자신 ($X[1]$)
- $S[2] = 2$: 자기 자신으로부터 이전 1개 요소 ($X[2]\leq X[2], X[1]\leq X[2]$)
- $S[3] = 3$: 자기 자신으로부터 이전 2개 요소 ($X[3]\leq X[3], X[2]\leq X[3], X[1]\leq X[3]$)
- $S[4] = 1$: 자기 자신 ($X[4]$)

첫 번째 알고리즘: $O(n^{2})$의 시간복잡도
```python
def spans1(X, n):
    # Input: n개의 정수를 갖는 배열 X
    # Output: X의 span을 갖는 배열 S
    S = [0 for _ in range(n)]
    for i in range(n):
        s = 1
        while s <= i and X[i - s] <= X[i]: # sum(1 ~ n-1)
            s = s + 1
        S[i] = s
    return S
```

두 번째 알고리즘: $O(n)$의 시간복잡도
* $i$를 현재 인덱스라고 했을 때
    1. $X[i] < X[j]$를 만족하는 인덱스 $j$를 찾을 때까지 스택에서 계속 pop을 반복한다.
    2. $S[j] \leftarrow i - j $
    3. $i$를 스택에 push한다.
* 각 배열의 인덱스는 스택에 정확히 한번만 push되고, 스택으로부터 많아야 한번 pop된다.
* while문 내 명령어는 많아야 $n$번 실행된다.
```python
def spans2(X, n):
    # Input: n개의 정수를 갖는 배열 X
    # Output: X의 span을 갖는 배열 S
    S = [0 for _ in range(n)]
    A = [] # Stack
    for i in range(n):
        while (not A.empty() and X[A.top()] <= X[i]):
            A.pop()
        if A.empty():
            S[i] = i + 1
        else:
            S[i] = i - A.top()
        A.push(i)
    return S
```

## 큐 (Queues)
---
삽입과 제거가 FIFO (First-in first-out) 방식을 따른다.
- 삽입은 큐의 가장 뒤에서 수행되고, 삭제는 큐의 가장 앞에서 수행된다.
- 주요 기능
    - $enqueue(object)$: 큐의 가장 뒤에 있는 요소 삽입
    - $dequeue()$: 큐의 가장 앞에 있는 요소 삭제
- 보조 기능
    - $front()$: 큐의 가장 앞에 있는 요소를 반환한다. (제거 X)
    - $size()$: 저장된 요소의 수를 반환한다.
    - $empty()$: 저장된 요소들이 존재하는지 여부를 반환한다.
- 예시
    - 대기 리스트
    - 프린터에서 공유 리소스 접근
    - 멀티프로그래밍
    - 라운드 로빈 (Round robin) 스케줄러

### 배열 기반 큐
![queue_1](../../../assets/images/2018-03-28-image-1.png)
<!-- {: width="250" } -->
원형 방식으로 크기 $N$을 갖는 배열을 사용하고, 앞 (front)과 뒤 (rear)를 기록하기 위해 세 가지 변수를 활용한다.
- $f$: 가장 앞에 있는 요소의 인덱스
- $r$: 가장 뒤에 있는 요소의 `한 칸 뒤`의 인덱스
- $n$: 요소의 수

```python
def size():
    return n
def empty():
    return n == 0
def enqueue(o):
    if size() == n - 1:
        raise QueueFull
    else:
        Q[r] = o
        r = (r + 1) % n
        n = n + 1
def dequeue():
    if empty():
        raise QueueEmpty
    else:
        f = (f + 1) % n
        n = n - 1
```

### 덱 (deque, Double-ended queue)
![queue_2](../../../assets/images/2018-03-28-image-2.png)

이중 연결 리스트로 구현할 수 있으며, 삽입 및 삭제 기능이 모두 $O(1)$의 시간복잡도를 갖는다.

|Operation|Time|
|---|---|
|size|$O(1)$|
|empty|$O(1)$|
|front, back|$O(1)$|
|insertFront, insertBack|$O(1)$|
|eraseFront, eraseBack|$O(1)$|

```python
def push_front(e):
    first_node = head.next
    e.prev = head
    e.next = first_node
    first_node.prev = e
    n = n + 1
def push_back(e):
    last_node = tail.prev
    e.prev = last_node
    e.next = tail
    last_node.next = e
    n = n + 1
def pop_front():
    fsecond_node = head.next.next
    fsecond_node.prev = head
    head.next = fsecond_node
    n = n - 1
def pop_back():
    lsecond_node = tail.prev.prev
    lsecond_node.next = tail
    tail.prev = lsecond_node
    n = n - 1
```