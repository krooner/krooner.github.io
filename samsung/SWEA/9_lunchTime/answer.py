from collections import deque
from itertools import product

T = int(input())

for t in range(T):
    N = int(input())

    board = []
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
    
    stairs = []
    users = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                users.append((i,j))
            if 2<=board[i][j]<=10:
                stairs.append((i, j, board[i][j]))
    
    answer = 1e10
    for case in product("01", repeat=len(users)):
        case = list(map(int, list(case)))
        dists = [[case[i], abs(users[i][0]-stairs[case[i]][0])+\
            abs(users[i][1]-stairs[case[i]][1])] for i in range(len(users))]
        dists = sorted(dists, key = lambda x: x[1])
        dists = deque(dists)
        gates = deque([])
        stair_state = {0: deque([]), 1: deque([])}

        elapsed_time = 0
        while True:

            if len(dists) == 0 and len(gates) == 0 and \
                sum([len(v) for v in stair_state.values()]) == 0:
                break

            for i in [0, 1]:
                for _ in range(len(stair_state[i])):
                    value = stair_state[i].popleft()
                    if value != 0:
                        stair_state[i].append(value-1)
            
            for _ in range(len(dists)):
                i, d = dists.popleft()
                if d == 0:
                    gates.append(i)
                else:
                    dists.append([i, max(0, d-1)])

            for _ in range(len(gates)):
                i = gates.popleft()
                if len(stair_state[i]) < 3:
                    stair_state[i].append(stairs[i][-1]-1)
                else:
                    gates.append(i)
            
            elapsed_time += 1

        answer = min(answer, elapsed_time)
    
    print(f"#{t+1} {answer}")