from collections import deque

def east(dice):
    answer = [0 for _ in range(6)]
    answer[0] = dice[4]
    answer[1] = dice[1]
    answer[2] = dice[0]
    answer[3] = dice[3]
    answer[4] = dice[5]
    answer[5] = dice[2]
    return answer

def south(dice):
    answer = [0 for _ in range(6)]
    answer[0] = dice[3]
    answer[1] = dice[0]
    answer[2] = dice[2]
    answer[3] = dice[5]
    answer[4] = dice[4]
    answer[5] = dice[1]
    return answer

def west(dice):
    answer = [0 for _ in range(6)]
    answer[0] = dice[2]
    answer[1] = dice[1]
    answer[2] = dice[5]
    answer[3] = dice[3]
    answer[4] = dice[0]
    answer[5] = dice[4]
    return answer

def north(dice):
    answer = [0 for _ in range(6)]
    answer[0] = dice[1]
    answer[1] = dice[5]
    answer[2] = dice[2]
    answer[3] = dice[0]
    answer[4] = dice[4]
    answer[5] = dice[3]
    return answer

N, M, K = list(map(int, input().split()))

# 동 - 남 - 서 - 북 (시계 방향)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

opposite = {
    0: 2,
    1: 3,
    2: 0,
    3: 1
}

# 위 - 정면 - 우면 - 뒤 - 좌면 - 아래
dice = [1, 5, 3, 2, 4, 6]
r, c = 0, 0
d = 0

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

total_score = 0
cnt = 0
while cnt < K:
    # move dice
    rr, cc = r + dr[d], c + dc[d]
    if not (0<=rr<N) or not (0<=cc<M):
        d = opposite[d]
        rr = r + dr[d]; cc = c + dc[d]
    r = rr; c = cc
    if d == 0:
        dice = east(dice)
    elif d == 1:
        dice = south(dice)
    elif d == 2:
        dice = west(dice)
    else:
        dice = north(dice)

    # get score of board
        # 인접한 동일 점수들의 합
    same_cnt = 0
    visited = set([(r, c)])
    score = board[r][c]
    checker = deque([(r, c)])
    while len(checker) > 0:
        for _ in range(len(checker)):
            pr, pc = checker.popleft()
            if board[pr][pc] == score:
                same_cnt += 1
            for i in range(4):
                prr, pcc = pr + dr[i], pc + dc[i]
                if not (0<=prr<N) or not (0<=pcc<M):
                    continue
                if (prr, pcc) not in visited and board[prr][pcc] == score:
                    visited.add((prr, pcc))
                    checker.append((prr, pcc))
    
    total_score += score * same_cnt

    # update d
    dice_bot = dice[-1]
    if dice_bot > score:
        d = (d+1)%4
    elif dice_bot < score:
        d = (d+3)%4
    
    cnt += 1

print(total_score)