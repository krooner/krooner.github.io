---
title: "Relations"
layout: post
parent: Discrete Math
grand_parent: School
nav_order: 4
date:   2018-03-27 14:30:00 +0900
---
# Relations
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

집합 $X$에서 $Y$로의 (이진, binary) 릴레이션 $R$은 Cartesian product $X\times Y$의 부분집합이다: $(x, y)\in R$일 때 $x R y$로 표기하고 $x$가 $Y$에 연관되었다고 한다.
- $X=Y$이면 $R$을 $X$에 대한 릴레이션이라 한다.
    - $R$을 $X=\\{1,2,3,4\\}$에 대한 릴레이션이라 한다면, $R=\\{(1,1), (1,2), (1,3), (1,4), (2,2), (2,3), (2,4), (3,3), (3,4), (4,4)\\}$
    - 방향 그래프 (directed graph)로 표현할 수 있다.

예 - $X=\\{2,3,4\\}, Y=\\{3,4,5,6,7\\}$일 때, 
- $R=\\{(2,4),(2,6),(3,3),(3,6),(4,4)\\}$
- $(x,y) \in R$ if $x$ divides $y$

## 특수 릴레이션
---
1. 모든 $x\in X$에 대해 $(x,x)\in R$이면 $X$에 대한 릴레이션 $R$은 `reflexive`하다.
2. 모든 $x, y\in X$에 대해 $(x,y)\in R$일 때 $(y,x)\in R$이면 $X$에 대한 릴레이션 $R$은 `symmetric`하다.
3. 모든 $x, y\in X$에 대해 $(x,y)\in R$이고 $(y,x)\in R$일 때 $x=y$이면 $X$에 대한 릴레이션 $R$은 `antisymmetric`하다.
4. 모든 $x, y, z\in X$에 대해 $(x,y), (y,z)\in R$일 때 $(x,z)\in R$이면 $X$에 대한 릴레이션 $R$은 `transitive`하다.

## 부분 순서 (Partial Order)
---
릴레이션 $R$이 `reflexive, antisymmetric, transitive`하면, 집합 $X$에 대한 릴레이션 $R$은 `partial order`이다.

- $x, y\in X$이면서, $x R y$이거나 $y R x$이면 $x,y$는 `comparable`하다.
- $x, y\in X$이면서, $x R y$도 $y R x$도 아니면 $x,y$는 `incomparable`하다.
- $X$의 모든 원소 쌍들이 comparable하면, $R$을 `total order`라고 한다.

## 동치 관계 (Equivalence Relations)
---
Theorem
- $S$를 집합 $X$의 partition (pairwise disjoint)이라 하자.
- $x R y$ (집합 내 어떤 집합 $A$에 대해 $x, y$ 모두 $A$에 속한다.)
- $R$은 `Reflexive, Symmetric, Transitive`

예 - $X=\\{1,2,3,4,5,6\\}, S = \\{\\{1,3,5\\}, \\{2, 6\\}, \\{4\\}\\}$일 때,
- $R=\\{(1,1),(1,3),(1,5),(3,1),(3,3),(3,5),(5,1),(5,3),(5,5),(2,2),(2,6),(6,2),(6,6),(4,4)\\}$

집합의 분할 (Partition)
- $R$을 집합 $X$에 대한 동치 관계라 하자.
- $a \in X$에 대해 $[a]=\\{x\in X\vert x R a\\}$
    - $[a]$는 $a$와 연관된 $X$ 내 모든 원소의 집합
- $S=\\{[a]\vert a\in X\\}$는 $X$의 partition이다.


## Inverse and Composition
---
$R$가 $X$에서 $Y$로의 릴레이션일 때, $R$의 inverse ($R^{-1}$)는 $Y$에서 $X$로의 릴레이션이다: $R^{-1}=\\{(y,x)\vert (x,y)\in R\\}$

$R_{1}$가 $X$에서 $Y$로의 릴레이션이고 $R_{2}$가 $Y$에서 $Z$로의 릴레이션일 때, $R_{1}, R_{2}$의 composition ($R_{1}\circ R_{2}$)는 $X$에서 $Z$로의 릴레이션이다: $R_{2}\circ R_{1}=\\{(x,z)\vert (x,y)\in R_{1} \text{ and } (y,z)\in R_{2} \text{ for some }y\in Y \\}$