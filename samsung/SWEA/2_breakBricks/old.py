dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

from copy import deepcopy

def removal(board, r, c, num):
    board[r][c] = 0
    for i in range(4):
        for j in range(1, num):
            rr, cc = r+dr[i]*j, c+dc[i]*j
            if rr<0 or rr>=len(board) or cc<0 or cc>=len(board[0]):
                break
            if board[rr][cc] != 0:
                newnum = board[rr][cc]
                board = removal(board, rr, cc, newnum)
    
    return board

def drop(board, col):
    r, c = len(board), len(board[0])
    
    idx = 0
    while True:
        if idx == r:
            return board
        if board[idx][col] != 0:
            break
        idx += 1
    
    number = board[idx][col]
    board = removal(board, idx, col, number)
    
    newboard = [[0 for _ in range(c)] for _ in range(r)]
    for col in range(c):
        col_walls = [board[i][col] for i in range(r) if board[i][col] != 0]
        col_walls.reverse()
        for i in range(len(col_walls)):
            newboard[-(i+1)][col] = col_walls[i]
    
    return newboard

def counting(board):
    r, c = len(board), len(board[0])
    answer = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0:
                answer += 1
    
    return answer

def solve(board, left, count):
    if left == 0:
        return count
    r, c = len(board), len(board[0])

    answer = count

    for col in range(c):
        newboard = drop(deepcopy(board), col)
        newcount = counting(newboard)
        if newcount == count:
            continue
        result = solve(newboard, left-1, newcount)
        answer = min(result, answer)

    return answer

T = int(input())

for t in range(T):
    N, W, H = list(map(int, input().split()))
    field = []
    for _ in range(H):
        row = list(map(int, input().split()))
        field.append(row)
    
    total = counting(field)
    answer = solve(deepcopy(field), N, total)
    
    print(f'#{t+1} {answer}')