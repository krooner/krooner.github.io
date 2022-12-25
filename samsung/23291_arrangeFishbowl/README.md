# 어항 정리
---

[Reference](https://www.acmicpc.net/problem/23291)

## Pointer를 잘 사용해야 한다.
- `row` (높이)
- `col` (어항의 시작, the leftmost index)
- `2개 이상의 multi-col, row을 방문하기 위한 Index`
- `나머지 single-col, row을 방문하기 위한 Index`

## 인접한 곳을 인덱싱하려면 결국은 2D Board를 만들어야 한다.
Board를 안 만들고, 유효한 값만 남기기 위해 list로 `.pop(), .append()`를 사용하기에는 너무 복잡

## 시간이 너무 오래 걸렸다.
어떤 원리로 진행되는지는 이해했는데, 어떤 자료구조로 접근해서 구현해야할지 고민되었다.

좀 더 문제를 많이 풀어봐야 할 필요를 느낀다.

시험장에서 만약 맞닥뜨렸다면 다른 문제를 먼저 풀었을 것 같다. 