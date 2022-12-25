from collections import deque
from collections import defaultdict

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
# -1: die, 0: empty, 1: live
for t in range(T):
    board = [[0 for _ in range(700)] for _ in range(700)]

    N, M, K = list(map(int, input().split()))
    queue = deque([])
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(len(row)):
            life = row[j]
            if life != 0:
                board[300+i][300+j] = 1
                queue.append([300+i, 300+j, life, life])

    for _ in range(K):
        length = len(queue)
        new_coor = defaultdict(list)
        for _ in range(length):
            r, c, curr, life = queue.popleft()
            curr -= 1
            if curr == -1:
                for i in range(4):
                    rr, cc = r+dr[i], c+dc[i]
                    if board[rr][cc] == 0:
                        new_coor[(rr, cc)].append(life)
            if curr == -life:
                board[r][c] = -1
                continue
            queue.append([r, c, curr, life])
        
        for k, v in new_coor.items():
            board[k[0]][k[1]] = 1
            queue.append([k[0], k[1], max(v), max(v)])
    
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                answer += 1
    
    print(f"#{t+1} {answer}")