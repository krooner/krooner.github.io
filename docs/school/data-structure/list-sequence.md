---
title: "List, Sequence"
layout: post
parent: Data Structure
grand_parent: School
nav_order: 5
date:   2018-04-04 14:30:00 +0900
---
# 리스트와 시퀀스
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 리스트
---
임의의 개체를 저장하는 위치들의 시퀀스를 모델링한 것으로, 위치 간의 이전/이후 관계를 형성한다.
- 일반적인 메소드: `size(), empty()`
- 업데이트 메소드: `insertFront(e), insertBack(e), removeFront(), removeBack()`
- 이중 연결 리스트를 기반으로 한 구현
    - 공간복잡도는 $O(n)$ ($n$개의 요소를 갖는 리스트)
    - 리스트의 각 위치의 공간 복잡도는 $O(1)$
    - 리스트의 모든 기능은 $O(1)$의 시간복잡도를 갖는다.

## 시퀀스
---
배열과 리스트를 활용한 것으로, 인덱스 또는 위치로 요소에 접근한다.
- 일반 메소드: `size(), empty()`
- 배열 리스트 기반 메소드: `at(i), set(i, o), insert(i, o), erase(i)`
- 리스트 기반 메소드: `begin(), end(), insertFront(o), insertBack(o), eraseFront(), eraseBack(), insert(p, o), erase(p)`
- Bridge 메소드: `atIndex(i), indexOf(p)`
