N = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

likes = {}
order = []
for _ in range(N*N):
    a, *b = list(map(int, input().split()))
    likes[a] = b
    order.append(a)

board = [[0 for _ in range(N)] for _ in range(N)]

def observe_cell(board, pos, std):
    # like std / empty contiguous / r / c
    r, c = pos
    like_cnt = 0
    empty_cnt = 0
    for i in range(4):
        rr, cc = r + dr[i], c + dc[i]
        if 0<=rr<N and 0<=cc<N:
            if board[rr][cc] == 0:
                empty_cnt += 1
            elif board[rr][cc] in likes[std]:
                like_cnt += 1

    return [like_cnt, empty_cnt, r, c]



def observe_board(board, std):
    answer = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                cell_info = observe_cell(board, (i, j), std)
                answer.append(cell_info)

    return answer

def scoring(pos, board, std):
    r, c = pos
    cnt = 0
    for i in range(4):
        rr, cc = r + dr[i], c+ dc[i]
        if 0<=rr<N and 0<=cc<N:
            if board[rr][cc] in likes[std]:
                cnt += 1

    if cnt == 0:
        return 0
    else:
        return pow(10, cnt-1)

for a in order:
    info = observe_board(board, a)
    info.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    _, _, r, c = info[0]
    board[r][c] = a

score = 0
for i in range(N):
    for j in range(N):
        std = board[i][j]
        score += scoring((i, j), board, std)

print(score)