T = int(input())

for t in range(T):
    N, X = list(map(int, input().split()))

    board = []
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
    
    cols = [[board[j][i] for j in range(N)] for i in range(N)]
    board += cols
    
    answer = 0
    for i in range(2*N):
        cnt = 1
        height = board[i][0]
        possible = True
        for j in range(1, N):
            if abs(height - board[i][j])>1:
                possible = False
                break
            if height - board[i][j] == 1: # DOWN
                if cnt >= 0:
                    cnt = 1 - X
                else:
                    possible = False
                    break
            elif height - board[i][j] == -1: # UP
                if cnt < X:
                    possible = False
                    break
                else:
                    cnt = 1
            else: # SAME
                cnt += 1
            height = board[i][j]
        if possible and cnt >= 0:
            answer += 1
    
    print(f"#{t+1} {answer}")

