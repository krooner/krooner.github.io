from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

def dfs(board, loc, N, length, visited):
    r, c = loc
    answer = length

    possible = False
    for i in range(4):
        rr, cc = r + dr[i], c + dc[i]
        if 0<=rr<N and 0<=cc<N:
            if visited[rr][cc] == 0 and board[rr][cc] < board[r][c]:
                possible = True
                visited[rr][cc] = 1
                result = dfs(board, [rr, cc], N, length+1, visited)
                answer = max(answer, result)
                visited[rr][cc] = 0
    
    if possible == False:
        return length

    return answer

        


for t in range(T):
    N, K = list(map(int, input().split()))

    board = []
    maxone = -1
    for _ in range(N):
        row = list(map(int, input().split()))
        maxone = max(maxone, max(row))
        board.append(row)
    
    maxlocs = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == maxone:
                maxlocs.append((i, j))
    
    answer = 0
    for i in range(N):
        for j in range(N):
            for d in range(1, K+1):
                board[i][j] -= d
                
                for loc in maxlocs:
                    visited = [[0 for _ in range(N)] for _ in range(N)]
                    height = dfs(board, loc, N, 1, visited)
                    answer = max(answer, height)

                board[i][j] += d

    print(f"#{t+1} {answer}")