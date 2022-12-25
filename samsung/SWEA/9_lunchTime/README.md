# [점심 식사시간](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl)

## 문제
...

## 풀이 방법
처리 순서
1. 이동 완료 여부 업데이트 $\rightarrow$ 계단 사용자 수 변화
2. 이동 시작할 사용자 선정

## Miscellaneous

```python
from itertools import product

for item in product((0, 1), repeat=N):
    # N명이 [0, 1] 중에 하나를 고르는 모든 경우
```
