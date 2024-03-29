---
title: "Proofs"
layout: post
parent: Discrete Math
grand_parent: School
nav_order: 2
date:   2018-03-13 14:30:00 +0900
--- 
# 증명
{: .no_toc }

<details open markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

공리 (Axioms): 증명 없이 일반적으로 참으로 여겨지는 명제
- 집합에 대한 공리 (집합 $X$에 대하여 $x \in X$)이자 명제

정의 (Definitions): 이미 존재하는 것으로부터 새로운 개념과 용어를 만들기 위해 사용
- $X \cup Y = \\{z \in U \vert z \in X \text{ or } z \in Y\\}$
- $z \in X \cup Y = z \in X \vee z \in Y$
- $X - Y = \\{z \in U \vert z \in X \text{ and } z \notin Y\\}$

정리 (Theorem): 참으로 증명된 명제
- 다른 정리를 증명하는데 유용하게 활용되며, 가설 $\rightarrow$ 결론의 형태이다.
- $X, Y$가 집합이면, $X\cup (Y-X) = X \cup Y$


증명은 가설부터 결론에 이르는, 논증 (logical argument) 으로 구성된 시퀀스이다.
- 검증된 사례들 (verified examples or cases)은 증명으로 간주되지 않는다.
- 추론 과정에서 여러 정리들은 이미 증명되었다고 가정할 수 있다.
- 명제가 거짓임을 보이는 예시를 반례 (counterexample)이라 한다.

## 직접 증명 (Direct Proof)
---
집합 연산이나 정의들을 활용해서 증명

### 반례를 활용한 증명 (Proof by Counterexample)
- 전체 한정된 명제 $\forall x P(x)$를 disprove하기 위해서는 $P(x)$가 거짓임을 보이는 논의영역 $D$의 원소 $x$ 하나만 보이는 것으로 충분하다.
- $(A\cap B)\cup C = A\cap(B\cup C)$를 disprove할 때,
    - 반례: $A=\emptyset, B=C=\\{1\\}$
    - $(A\cap B)\cup C = \\{1\\} \neq A\cap(B\cup C) = \emptyset$

## 간접 증명 (Indirect Proof)
---
### 대우를 활용한 증명 (Proof by Contrapositive)
- $p \rightarrow q \equiv \neg q \rightarrow \neg p$
- $p \rightarrow q$를 증명하기 위해서 $q \rightarrow \neg p$임을 보인다.
- $3n+2$가 홀수면, $n$은 홀수이다 라는 정리가 있다.
    - 정리의 결론을 거짓이라 하자 - `n은 짝수이다.`
    - 어떤 정수 $k$에 대하여 $n = 2k$이므로, $3n+2 = 3(2k)+2 = 6k+2 = 2(3k+1)$가 되어 $3n+2$는 홀수가 아니다

### 모순을 활용한 증명, 귀류법 (Proof by Contradiction)
- $p \rightarrow q \equiv \neg p \vee q \equiv \neg(p\wedge\neg q) \equiv (p\wedge\neg q) \rightarrow (r\wedge \neg r)$
- $p \rightarrow q$를 증명하기 위해, $(p\wedge\neg q)$로 가정하는 것이 모순이라는 것을 보인다.
$3n+2$가 홀수면, $n$은 홀수이다 라는 정리가 있다.
    - $3n+2$가 홀수이고 $n$은 짝수라고 하자: $(p\wedge\neg q)$
    - 위에서 보았듯 $n$이 짝수이면 $3n+2$도 짝수이다.
    - $3n+2$가 홀수라는 가정은 모순을 유발하므로, 해당 정리는 증명됨.
- 무한한 논의영역으로 갖는 전체 한정된 명제를 증명하는데 활용됨
    - $\forall x \neg P(x)$를 증명하기 위해서, $\exists x P(x)$가 모순임을 보이는 것으로 충분.

### 케이스 증명 (Proof by Cases)
$p$가 $p_{1}\vee p_{2} \vee \cdot\cdot\cdot\vee p_{n}$와 동치일 때, $p\rightarrow q$를 증명하는 것은 모든 $i$에 대해 $p_{i} \rightarrow q$를 증명하는 것으로 충분하다.
- 적어도 하나의 $p_{i}$가 참일 때 $\text{iff } p$는 참이다.
- $(p_{1}\vee \cdot\cdot\cdot\vee p_{n})\rightarrow q$를 보이는 대신에, $(p_{1}\rightarrow q)\wedge\cdot\cdot\cdot\wedge(p_{n}\rightarrow q)$임을 보인다.
- $x, y$가 실수일 때 $\vert xy\vert=\vert x \vert\vert y\vert$이다.
    - $p$: $x, y \in \mathbb{R}, q: \vert xy\vert=\vert x \vert\vert y\vert$
    - $p$는 $p_{1}\vee p_{2}\vee p_{3}\vee p_{4}$이며,
        - $p_{1}: x\geq0, y\geq0$, $p_{2}: x\geq0, y<0$
        - $p_{3}: x<0, y\geq0$, $p_{4}: x<0, y<0$
    - $p\rightarrow q$ 대신에 $(p_{1}\rightarrow q)\wedge(p_{2}\rightarrow q)\wedge(p_{3}\rightarrow q)\wedge(p_{4}\rightarrow q)$

### 동치 증명 (Proofs of Equivalence)
- $p\iff q \equiv (p\rightarrow q)\wedge (q \rightarrow p)$
- $p_{1}, p_{2}, p_{3}$이 모두 동치 iff $(p_{1}\rightarrow p_{2})\wedge(p_{2}\rightarrow p_{3})\wedge(p_{3}\rightarrow p_{1})$

### 존재 증명 (Existence Proofs)
- $\exists x P(x)$에 대한 증명으로, $a, b$가 $a<b$를 만족하는 실수일 때 $a<x<b$를 만족하는 실수 $x$가 존재함을 증명
    - 실수 $\frac{a+b}{2}$는 $a<\frac{a+b}{2}<b$를 만족
- Constructive: 특정 성질을 갖는 원소가 존재함을 explicit하게 찾는 방식 (e.g. $\frac{a+b}{2}$)
- Non-constructive: 특정 성질을 갖는 원소가 존재함을 explicit하게 찾지 못함 (e.g. 모순을 활용한 증명)
    - 유리수 $x^{y}$를 만드는 무리수 $x, y$가 존재함을 보여라.
    - $x = \sqrt{2}^{\sqrt{2}}, y=\sqrt{2} \rightarrow x^{y}=(\sqrt{2}^{\sqrt{2}})^{\sqrt{2}}=2$

## 귀납과 연역 (Induction and Deduction)
---
귀납 추론 (inductive reasoning): 일반적인 법칙을 support하는 증거들을 모은다.
- 과학적 발견들은 귀납 추론에 의한 것
- 수학적으로는 `올바르지 않은` 예시에 의한 증명

연역 추론 (deductive reasoning): 결론의 진리값은 주어진 전제들의 논리적 결과이다.
- 모든 수학적 논증은 연역적이다.
- 모든 수학적 정리는 조건부 명제 형태로 주어진다.
- 공리는 연쇄적인 연역 추론의 첫 시작점으로 주어진다.

### 수학적 귀납법 (Mathematical Induction)
이름은 귀납법이지만, `연역 추론` 방식이다.

양의 정수 $n \in Z^{+}$에 대하여 $\forall n S(n)$을 증명하기 위해 $\forall n S(n) \rightarrow S(n+1)$을 보인다. 해당 논증의 유효성은 정수 집합의 기본적인 특성이다. 

수학적 귀납법은 특정 방식으로 얻어진 결과를 증명하는 데에만 활용되며, 공식 또는 정리를 규명하기 위한 도구는 아니다.

* 양의 정수 집합을 논의영역 $D$로 하는 명제 함수 $S(n)$이 있다고 가정할 때,
    - $S(1)$이 참이라 가정한다 (Basis Step)
    - $n\geq1$에 대하여 $S(n)$이 참이면 $S(n+1)$도 참이다 (Inductive Step)
    - 그러면 $S(n)$은 모든 양의 정수 $n$에 대하여 참이다.

즉, $n \in Z^{+}$에 대해 $\forall n S(n) \leftarrow S(1) \wedge (\forall n(S(n) \rightarrow S(n+1)))$

예 - $5^{n}-1$은 모든 $n\geq 1$에 대하여 4로 나눠진다.
- Basis Step: $n=1$일 때 $5^{n}-1=4$는 4로 나눠짐.
- Inductive Step: 어떤 정수 $k$에 대하여 $5^{n}-1=4k$라 가정하면, $5^{n+1}-1=5(4k+1)-1=4(5k+1)$이므로 4로 나눠짐.

따라서, 수학적 귀납법에 의하여 $5^{n}-1$은 모든 $n\geq 1$에 대하여 4로 나눠진다.

### Strong Form of Induction
모든 이전 명제들의 참을 가정하며, inductive step에서 $1\leq k < n$ 인 $S(k) \rightarrow S(n)$ 
* $\forall n S(n-1) \rightarrow S(n)$ 보다는 약한 명제 (weaker statement)
* $S(n-1) \rightarrow S(n)$가 참이면 $1\leq k < n$ 인 $S(k) \rightarrow S(n)$도 참

$\geq n_{0}$인 정수 집합을 논의영역 $D$로 하는 명제 함수 $S(n)$이 있다고 가정할 때,
- $S(n_{0})$이 참이라 가정한다 (Basis Step)
    - $P(1), P(2), ... P(k)$는 참이다.
- $n>n_{0}$에 대하여 $n_{0}\leq k<n$ 인 $S(k)$가 참이면, $S(n)$도 참이다 (Inductive Step)
    - 모든 가능한 정수 $k$에 대하여 $P(1) \wedge P(2) \wedge ... \wedge P(k) \rightarrow P(k+1)$
- 그러면 $S(n)$은 모든 정수 $n\geq n_{0}$에 대하여 참이다.

### 정렬성 (Well-Ordering Property for nonnegative integers)
1. 공집합이 아닌 자연수 집합은 가장 작은 원소를 갖는다.
2. 모든 음이 아닌 정수 집합은 가장 작은 원소를 갖는다.

정렬성을 수학적 귀납법으로 증명할 수 있고, 수학적 귀납법 또한 정렬성을 이용하여 증명할 수 있다. - 서로 동치이다.