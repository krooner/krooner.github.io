# 마법사 상어와 블리자드
---

[Reference](https://www.acmicpc.net/problem/21611)

## 변수 업데이트 및 체크
기본에 충실합시다. 결국은 연습, 또 연습.

**잘못된 예시**
- Position을 업데이트 하지 않고 똑같은 Position을 다시 비교

```python

while True:
        for _ in range(2): # repeat two
            for _ in range(move): 
                if not (0<=cr<N) or not (0<=cc<N) or idx == len(new_beads):
                    return 
                cr += rdr[cd]; cc += rdc[cd]
                board[cr][cc] = new_beads[idx]
                idx += 1
            cd = (cd+1)%4
        move += 1

```

**올바른 예시**
- Position을 업데이트 한 다음 새로운 Position을 비교

```python
while True:
        for _ in range(2): # repeat two
            for _ in range(move): 
                cr += rdr[cd]; cc += rdc[cd]
                if not (0<=cr<N) or not (0<=cc<N) or idx == len(new_beads):
                    return 
                board[cr][cc] = new_beads[idx]
                idx += 1
            cd = (cd+1)%4
        move += 1
```