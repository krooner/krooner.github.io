T = int(input())

for t in range(T):
    N, M = list(map(int, input().split()))

    board = []
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
    
    houses = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                houses.append((i, j))

    h = len(houses)
    max_house = -1
    for r in range(N):
        for c in range(N):
            distances = []
            for j in range(h):
                dist = abs(houses[j][0]-r) + abs(houses[j][1]-c)
                distances.append(dist)
            limit = max(distances)

            for j in range(1, limit+2):
                cost = j*j + (j-1)*(j-1)
                counts = sum([1 for item in distances if item<j])
                if counts*M - cost >= 0:
                    max_house = max(max_house, counts)
    
    print(f"#{t+1} {max_house}")