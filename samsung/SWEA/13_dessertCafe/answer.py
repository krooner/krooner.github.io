T = int(input())

order = {0: [-1, 1], 1: [1, 1], 2: [1, -1], 3: [-1, -1]}

def traverse(board, r, c, h, v, N):
    curr = [r, c]
    eat = set([board[r][c]])
    for key in order.keys():
        itr = h if key%2 == 0 else v 
        for i in range(itr):
            curr[0] += order[key][0]
            curr[1] += order[key][1]
            if (not (0<=curr[0]<N)) or (not (0<=curr[1]<N)):
                return -1
            newd = board[curr[0]][curr[1]]
            if newd in eat:
                if key == 3 and i == itr-1:
                    pass
                else:
                    return -1
            eat.add(newd)
    assert curr[0] == r and curr[1] == c

    return len(eat)

for t in range(T):
    N = int(input())

    board = []
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
    
    answer = -1
    for i in range(N):
        for j in range(N):
            for h in range(1, N-1):
                for v in range(1, N-1):
                    result = traverse(board, i, j, h, v, N)
                    answer = max(result, answer)
    
    print(f"#{t+1} {answer}")