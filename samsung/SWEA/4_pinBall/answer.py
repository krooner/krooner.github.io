from collections import defaultdict

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())


convert = {
    # (block_num, before_dir): after_dir
    (1, 0): 2,
    (1, 1): 3,
    (1, 2): 1,
    (1, 3): 0,
    (2, 0): 1,
    (2, 1): 3,
    (2, 2): 0,
    (2, 3): 2,
    (3, 0): 3,
    (3, 1): 2,
    (3, 2): 0, 
    (3, 3): 1,
    (4, 0): 2,
    (4, 1): 0,
    (4, 2): 3,
    (4, 3): 1,
    (5, 0): 2,
    (5, 1): 3,
    (5, 2): 0, 
    (5, 3): 1
}

def solve(board, wormholes, r, c, d):
    sr, sc = r, c
    pscore = 0
    n = len(board)
    r += dr[d]
    c += dc[d]
    while True:
        if 0<=r<n and 0<=c<n: # Wall
            if (r == sr and c == sc) or board[r][c] == -1: # Termination
                break
            
            elif 1<=board[r][c]<=5: # Block
                pscore += 1
                d = convert[(board[r][c], d)]
            
            elif 6<=board[r][c]<=10: # Hole
                l = wormholes[board[r][c]]
                if l[0] != (r, c):
                    r, c = l[0]
                else:
                    r, c = l[1]
        else:
            pscore += 1
            d = (d+2)%4
        
        r += dr[d]
        c += dc[d]
        


    return pscore

for t in range(T):
    N = int(input())
    board = []

    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)


    wormholes = defaultdict(list)

    for i in range(N):
        for j in range(N):
            if board[i][j] >= 6:
                wormholes[board[i][j]].append((i, j))
    
    answer = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    score = solve(board, wormholes, i, j, k)
                    # print(score)
                    answer = max(score, answer)
    
    print(f"#{t+1} {answer}")

