# 보호 필름
---

[URL](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu)

### 브루트 포스, DFS
1. 재귀 방식
2. 반복 방식

```python

from itertools import product

for item in product((0, 1), repeat=len(choose)):
    # 선택된 막에 대하여 A 또는 B 특성 선택

```

### for-else 문
nested for-loop에 활용된다.
- e.g. for-loop을 수행하다가 `break`에 의해 loop를 빠져나온 경우

```python

for dr in range(1, K):
    # ...

else:
    break

```
