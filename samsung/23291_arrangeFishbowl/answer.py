# 어항 정리: https://www.acmicpc.net/problem/23291
from collections import defaultdict
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def arrange(bowls, N):
    min_fish = min(bowls)

    for i in range(N):
        if bowls[i] == min_fish:
            bowls[i] += 1

    board = [[-1 for _ in range(N)] for _ in range(100)]
    board.append(bowls)
    
    bot = 100
    w, h = 0, 0
    value = board[bot][w]
    board[bot][w] = -1
    w += 1
    h += 1
    board[bot-h][w] = value
    
    while True:
        e = w
        while True:
            if e == N:
                break
            if board[bot-h][e] != -1:
                e += 1
            else:
                break
        
        if N-e < h+1:
            break

        length = e-w
        for i in range(length):
            multi_col = e-i-1
            multi_row = bot
            single_row = bot-i-1
            single_col = e
            while board[multi_row][multi_col] != -1:
                value = board[multi_row][multi_col]
                board[single_row][single_col] = value
                board[multi_row][multi_col] = -1
                multi_row -= 1
                single_col += 1

        h = bot - single_row
        
        w += length

    dict_ = defaultdict(list)
    
    # ONLY RECEIVE
    for c in range(w, N):
        for r in range(bot-h, bot+1):
            center = board[r][c]
            if center != -1:
                for i in range(4):
                    rr, cc = r + dr[i], c + dc[i]
                    if 0<=rr<=bot and 0<=cc<N:
                        if board[rr][cc] != -1 and center < board[rr][cc]:
                            q = (board[rr][cc]-center)//5
                            if q > 0:
                                dict_[(r, c)].append(q)
                                dict_[(rr, cc)].append(-q)
    
    for k, v in dict_.items():
        r, c = k
        board[r][c] += sum(v)
    
    flatten = []
    for c in range(w, N):
        r = bot
        while board[r][c] != -1:
            flatten.append(board[r][c])
            r -= 1

    a, b = flatten[:int(N/2)], flatten[int(N/2):]
    a.reverse()
    l = [a, b]

    left_block = []
    right_block = []
    half = len(l[0])
    for j in range(len(l)):
        left_row = [l[j][i] for i in range(0, int(N/4))]
        left_block.append(left_row)
        right_row = [l[j][i] for i in range(int(N/4), half)]
        right_block.append(right_row)

    l = deque([])
    for i in range(len(left_block)-1, -1, -1):
        row = left_block[i]
        row.reverse()
        l.append(row)
    for i in range(len(right_block)):
        l.append(right_block[i])

    dict_ = defaultdict(list)
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            center = l[r][c]
            for i in range(4):
                rr, cc = r + dr[i], c + dc[i]
                if 0<=rr<len(l) and 0<=cc<len(l[0]):
                    counter = l[rr][cc]
                    if counter > center:
                        q = (counter-center)//5
                        if q > 0:
                            dict_[(r, c)].append(q)
                            dict_[(rr, cc)].append(-q)
    
    for k, v in dict_.items():
        r, c = k 
        l[r][c] += sum(v)
    
    flatten = []
    for c in range(len(l[0])):
        col = []
        for r in range(len(l)):
            col.append(l[r][c])
        col.reverse()
        flatten += col
    
    return flatten

N, K = list(map(int, input().split()))
bowls = list(map(int, input().split()))

cnt = 0
while True:
    if max(bowls) - min(bowls) <= K:
        break
    else:
        bowls = arrange(bowls, N)
        cnt += 1

print(cnt)