# [벽돌 깨기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo)

## 문제
구슬을 쏘아 벽돌을 꺠트리는 게임을 하려고 한다. 구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 아래와 같이 $w\times h$ 배열로 주어진다. (0은 빈 공간을 의미하며, 그 외의 숫자는 벽돌을 의미한다.)

게임의 규칙은 다음과 같다.
1. 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.
2. 벽돌은 숫자 1-9로 표현되며, 구슬이 명중한 벽돌은 상하좌우로 (벽돌에 적힌 숫자 - 1) 칸 만큼 같이 제거된다.
3. 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.
4. 빈 공간이 있을 경우 벽돌은 밑으로 떨어지게 된다.

N개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다. N, W, H 그리고 벽돌 정보가 주어질 때 남은 벽돌의 개수를 구하라.



## 풀이 방법
- **2차원 배열 복사는 deepcopy** - `array[:]`로 뻘짓했다.

```python
from copy import deepcopy

2d_array_copy_wrong = array[:]
2d_array_copy_right = deepcopy(array)
```

- 중간 과정에 조건을 집어넣어서 최대한 최적화를 시도하다가는 오히려 꼬여버리는 수가 있다
    - 벽돌이 존재하지 않는 column을 체크하는 과정을 넣는 등..
- **입력값의 범위를 보고 크지 않으면 일단 Raw하게 구현을 하자!**
---

N 개의 벽돌을 떨어트려 **최대한 많은 벽돌을 제거**... $\rightarrow$ DFS

- 돌을 다 쓸 때까지 실행되도록 `Recursion`을 활용한다.
- **최대한 많은 벽돌 제거 = 벽돌을 최소한으로 남긴다**
    - 함수의 argument로 벽돌을 제거시킨 후의 board의 잔여 벽돌 갯수를 갖고 간다: `count`
    - `answer = min(answer, count)`
- 벽돌이 부서지자마자 바로 해당 column을 update하지 않고, 연쇄 작용이 모두 끝날 때 한꺼번에 update한다
    1. 새로운 board를 initialize한다.
    2. 기존 board의 column에서 남은 벽돌을 확인한다.
    3. 새로운 board를 update한다.






