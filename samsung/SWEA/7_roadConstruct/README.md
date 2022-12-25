# [활주로 건설](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH)

## 문제
... (ing)

## 풀이

[Reference: YouTube](https://youtu.be/D3LCf9tD9Cs)

연속적으로 높이가 유지되는 길이를 저장한다.
1. 값이 증가하는 경우 - **현재 값**에 따라 활주로를 사용
    - 현재 값이 활주로 사용에 부족하면 $False$
    - 활주로 사용이 가능하면 차감
2. 값이 감소하는 경우 - 활주로를 **미리 사용**
    - 마지막 부분에서 값이 음수인 경우 $False$

$\therefore$ 문제를 계속 풀어야지만 알 수 있는 직관!

