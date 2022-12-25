from collections import deque

N = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

board = [list(map(int, list(input()))) for _ in range(N)]

def dfs(board, r, c):
    count = 1
    board[r][c] = -1
    dq = deque([(r, c)])
    while len(dq) != 0:
        for _ in range(len(dq)):
            rr, cc = dq.popleft()
            for i in range(4):
                nr, nc = rr + dr[i], cc + dc[i]
                if 0<=nr<N and 0<=nc<N and board[nr][nc] == 1:
                    count += 1
                    board[nr][nc] = -1
                    dq.append((nr, nc))

    return count

answers = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            answers.append(dfs(board, i, j))

answers.sort()
print(len(answers))
for item in answers:
    print(item)


    