from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

H, W = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(H)]

commands = []
Q = int(input())
for _ in range(Q):
    r, c, v = list(map(int, input().split()))
    r -= 1
    c -= 1
    commands.append((r, c, v))

def change(r, c, from_, to_):
    dq = deque([(r, c)])
    board[r][c] = to_
    while len(dq) != 0:
        for _ in range(len(dq)):
            rr, cc = dq.popleft()
            for i in range(4):
                nr, nc = rr + dr[i], cc + dc[i]
                if 0<=nr<H and 0<=nc<W and board[nr][nc] == from_:
                    board[nr][nc] = to_
                    dq.append((nr, nc))
    
    return

for r, c, v in commands:
    origin = board[r][c]
    if origin != v:
        change(r, c, origin, v)

for row in board:
    print(" ".join(list(map(str, row))))
