---
title: "Sets and Logic"
layout: post
parent: Discrete Math
grand_parent: School
nav_order: 1
date:   2018-03-06 14:30:00 +0900
---
# 집합과 논리학
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## 집합 (Set)
---
순서 없이 수집된 개체들 (e.g. A반의 학생들, 교실의 모든 의자)
* 원소 (element or member): 집합 내 개체
* 집합 $A$은 원소 $a$를 포함한다: $a \in A$
    * Otherwise, $a \notin A$
* 표현 방법
    * 모든 원소 열거 $A=\\{ 1,2,3,4\\}$
    * 집합에 속하기 위한 특성을 열거 $B=\\{x \vert x \text{ 는 양의 정수이면서 짝수 } \\}$

### 전체 집합과 공집합 (Universal set and Empty set)
* 전체 집합 $U$: 현재 고려되는 모든 원소를 포함
* 공집합 ($\emptyset$ 또는 $\\{\\}$): 원소가 없음
* 집합은 다른 집합의 원소가 될 수 있음: $\\{\\{1,2,3\\}, a, \\{b,c\\}\\}$
* 공집합은 `공집합을 포함하는 집합`과 다름: $\emptyset \neq \\{\emptyset\\}$

집합의 크기 (Cardinality): 집합의 원소 갯수에 대한 척도
* $X$가 유한한 집합일 때, $\vert X\vert$ = 집합 $X$의 원소 갯수

### 집합 일치와 부분집합 (Set Equality and Subset)
두 집합 $X, Y$이 같은 원소로 구성되어 있으면, 서로 같은 집합이며, 역 또한 성립한다 (iff - if and only iff): $X = Y$
- For every $a$, if $a \in X$, then $a \in Y$, and
for every $a$, if $a \in Y$, then $a \in X$.

집합 $A$의 모든 원소가 집합 $B$의 원소라면, $A$는 $B$의 부분집합이다 (iff).
- 부분집합 $A\subseteq B$
- 진부분집합 (Proper subset) $A\subset B$
    * 자기 자신 (집합 $B$)를 제외한 모든 부분집합

### 멱집합 (Power Set)
집합 $X$의 모든 부분집합을 원소로 갖는 집합: $P(X)$
* $A=\\{a,b,c\\}$ 일 때, $P(X)$의 원소는 $\emptyset, \\{a\\}, \\{b\\},\\{c\\},\\{a,b\\},\\{a,c\\},\\{b,c\\},\\{a,b,c\\}$
* $\\{a,b,c\\}$를 제외한 원소들은 $A$의 진부분집합
* $\vert X\vert=n$이면, $\vert P(X)\vert=2^{n}$

### 집합 연산 (Set Operations)
- 합집합 (Union): $X\cup Y = \\{x\vert x\in X \text{ or } x \in Y\\}$
- 교집합 (Intersection): $X\cap Y = \\{x\vert x\in X \text{ and } x \in Y\\}$
- 차집합 (Difference or Relative complement): $X - Y = \\{x\vert x\in X \text{ and } x \notin Y\\}$
- 여집합 (Complement): $\bar A = \\{x\in U \vert x \notin A\\}$

Union and Intersection: `임의의 집합들로 구성된 집합 S`가 있을 때,

합집합 - 원소 $x$는 최소 $S$ 내 하나의 집합 $X$에 속해야 한다.
$\cup S=\\{x\vert x\in X \text{ for some } X \in S\\}$

교집합 - 원소 $x$는 $S$ 내 모든 집합 $X$에 속해야 한다.
$\cap S=\\{x\vert x\in X \text{ for all } X \in S\\}$

### 집합의 분할 (Partition)
집합 $X$의 공집합이 아닌 부분집합들로 구성된 $S$가 있을 때, $X$내 모든 원소가 오직 $S$의 원소 중 하나에만 속해있는 경우 - $S$는 집합 $X$의 Partition이다.
* $S$는 $X$를 서로 중첩되지 않는 (nonoverlapping) 부분집합들로 분리한다.
* $S$는 서로소 (Pairwise disjoint)이며 $\cap S = X$

$X=\\{\text{pink, yellow, skyblue, purple}\\}$일 때, <br>
$W = \\{\text{pink, yellow}\\}, C = \\{\text{skyblue, purple}\\}$

$S=\\{W, C\\}=\\{\\{\text{pink, yellow}\\}, \\{\text{skyblue, purple}\\}\\}$ <br>
$\cup S = \\{\text{pink, yellow, skyblue, purple}\\}$ <br>
$\cap S = \emptyset$

### Cartesian Product
Ordering in Sets
* 원소의 순서쌍: $a=b$의 경우를 제외하면 $(b, a)$는 $(a, b)$와 다르다

Cartesian Product
* 집합 $X, Y$가 있을 때, $X\times Y$는 모든 순서쌍의 집합이다.
    * $A\times B=\\{(a,b)\vert a\in A \wedge b\in B\\}$
* $X=\\{1,2,3\\}, Y=\\{a, b\\}$일 때, <br>
$X\times Y=\\{(1, a), (1, b), (2, a), (2, b), (3, a), (3, b)\\}$ <br>
$Y\times X=\\{(a, 1), (b, 1), (a, 2), (b, 2), (a, 3), (b, 3)\\}$ <br>
$X\times X=\\{(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3,1), (3,2), (3,3)\\}$ <br>
$Y\times Y=\\{(a, a), (a, b), (b, a), (b, b)\\}$
* $A_{1}\times A_{2}\times ... \times A_{n}$ = $\\{(a_{1}, a_{2}, ..., a_{n})\vert a_{i} \in A_{i} \text{ for } i = 1,2,...,n\\}$
    * $N$-tuple: $(a_{1}, a_{2}, ..., a_{n})$
    * $\vert A_{1}\times A_{2}\times ... \times A_{n}\vert$ = $\vert A_{1}\vert\cdot\vert A_{2}\vert\cdot...\cdot\vert A_{n}\vert$

## 논리학 (Logic)
---
추론 (Reasoning)을 위한 학문으로, 추론이 올바른지를 구체적으로 다루며 명제 간의 관계에 초점을 맞춤

### 명제 (Propositions)
명제 (proposition or statement): 참이거나 거짓 둘 중에 하나인 문장 (~~참이면서 거짓~~)

$p, q$를 명제라고 했을 때,
* 논리곱 (conjunction): $p \wedge q = p \text{ and } q$
* 논리합 (disjunction): $p \vee q = p \text{ or } q$

연산자 우선순위: $\neg \rightarrow \wedge \rightarrow \vee$

### 조건부 명제 (Conditional Propositions)
$p, q$가 명제일 때, 명제 [if $p$ then $q$]는 조건부 명제이다.
- $p \text{ (hypothesis) } \rightarrow q \text{ (conclusion) }$

$p\text{ only if }q$: $p \rightarrow q$ <br>
$p\text{ if and only if }q$: $(p \rightarrow q) \text{ and } (p \rightarrow q)$

### 등치 명제 (Biconditional Proposition)
$p, q$가 명제일 때, 명제 [$p$ if and only if $q$]는 등치 명제이다.
- $p \text{ (hypothesis) } \iff q \text{ (conclusion) }$
- $p \Rightarrow q \text{ and }q \Rightarrow p$ 와 논리적 동치 (logically equivalent)

### 논리적 동치 (Logically Equivalent)
명제 $P, Q$가 다른 명제들 $p_{1}, ..., p_{n}$으로 만들어졌을 때, $p_{1}, ..., p_{n}$의 진리값에 따라 $P, Q$의 진리값이 항상 일치하는 경우: $P \equiv Q$

예를 들어 $P = \neg (p \vee q)$, $Q = \neg p \wedge \neg q$ <br>

|$p$|$q$|$\neg (p \vee q)$|$\neg p \wedge \neg q$|
|---|---|---|---|
|T|T|**F**|**F**|
|T|F|**F**|**F**|
|F|T|**F**|**F**|
|F|F|**T**|**T**|
    
- 항상 참인 명제 (tautology): 두 개 이상의 명제로 구성된 합성 명제 (compound proposition)으로, 명제에서 발생 가능한 진리값과 관계없이 항상 참
- $p \iff q$ 가 tautology라면, 명제 $p, q$는 논리적 동치이다.

### 대우 (Contrapositive or Transposition)
조건부 명제 $p \rightarrow q$의 대우는 $\neg q \rightarrow \neg p$
* $p \rightarrow q$와 $\neg q \rightarrow \neg p$는 논리적 동치

조건부 명제의 역 (converse)는 단지 $p, q$의 역할만 뒤바꿨지만, 대우는 $p, q$의 역할을 뒤바꾼뒤 각각에 대해 부정 (이, inverse)를 적용함.
- 역 (converse): $q\rightarrow p$
- 이 (inverse): $\neg p \rightarrow \neg q$

### 논증 (Arguments)
명제들의 시퀀스로, 다음과 같이 표현한다.

$p_{1},p_{2},...,p_{n} \text{ (hypotheses) }/\therefore q \text{ (conclusion) }$

* $p_{1}, ..., p_{n}$이 모두 참일 때 $q$도 참인 경우 Argument는 유효 (valid) 하다. 그렇지 않은 경우는 유효하지 않다 (invalid or a fallacy).

### 한정자 (Quantifiers)
$P(x)$를 변수 $x$와 연관된 명제이고 $D$를 집합이라 할 때, 
* $D$의 각 원소 $x$에 대해 $P(x)$가 명제인 경우, $P$를 $D$에 대한 명제함수 (propositional function or predicate)이라 한다.
* $D$는 $P$의 논의영역 (domain of discourse)이다.

예 - $P(x)$: $x$는 홀수인 정수이다.
* $P$는 $Z^{+}$를 논의 영역으로 갖는 명제함수이다.
    * $P(1)$: 1은 홀수인 정수이다 - $True$
    * $P(2)$: 2은 홀수인 정수이다 - $False$
    * ...

#### 전체 한정자 (Universal Quantifier)
논의영역 $D$를 갖는 명제함수 $P$가 있을 때, 
* $\text{for every } x, P(x)$를 전체 한정된 명제 (universally quantified statement)라 한다 - $\forall x P(x)$
* $D$의 모든 원소 $x$에 대해 $P(x)$가 참이면 $\forall x P(x)$는 참이다.
* $D$의 모든 원소 중 적어도 하나의 원소 $x$에 대해 $P(x)$가 거짓이면 $\forall x P(x)$는 거짓이다.

#### 존재 한정자 (Existential Quantifier)
논의영역 $D$를 갖는 명제함수 $P$가 있을 때, 
* $\text{there exists } x, P(x)$를 존재 한정된 명제 (existentially quantified statement)라 한다 - $\exists x P(x)$
* $D$의 모든 원소 중 적어도 하나의 원소 $x$에 대해 $P(x)$가 참이면 $\exists x P(x)$는 참이다.
* $D$의 모든 원소 $x$에 대해 $P(x)$가 거짓이면 $\exists x P(x)$는 거짓이다.

#### 중첩 한정자 (Nested Quantifiers)
예 - $L(x, y)$: $x$는 $y$를 사랑한다.

`모든 사람은 누군가를 사랑한다`
- 모든 사람 $x$에 대해, $x$가 사랑하는 사람 $y$가 존재한다.
    * $\forall x\exists y L(x, y)$
- $\exists x\forall y L(x, y)$
    * 모든 사람 $y$에 대해 $y$를 좋아하는 사람 $x$가 존재한다.
    * `누군가는 모든 사람을 사랑한다`

### 공진리 (Vacuous Truth)
그릇 안이 비어있을 때, `그릇 내 모든 공들은 파란색이다`라는 명제는 참인가 거짓인가?

명제 $p$는 명제의 부정 (negation)이 참일 때 거짓. <br>
$\neg p$: `그릇 안에는 파란색이 아닌 공이 존재한다.` <br>
명제의 부정이 거짓이므로, 해당 명제는 `기본적으로 (by default)` 참이다.

$\forall x \text{ in } D, \text{ if } P(x) \text{ then } Q(x)$ 형태의 명제는, $D$의 모든 원소 $x$에 대해 $P(x)$가 거짓인 경우 공진리 (vacuously true OR true by default)이다.