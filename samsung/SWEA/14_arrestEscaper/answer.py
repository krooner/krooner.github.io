from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

blocks = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 1],
    5: [1, 2],
    6: [2, 3],
    7: [3, 0]
}

opposite = {
    0: 2,
    2: 0,
    1: 3,
    3: 1
}


T = int(input())
for t in range(T):
    N, M, R, C, L = list(map(int, input().split()))
    board = []
    loc = [R, C]
    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
    
    locs = set()
    status = deque([(R, C)])
    elapsed = 0
    while elapsed < L:
        for _ in range(len(status)):
            r, c = status.popleft()
            bnum = board[r][c]
            locs.add((r, c))
            for d in blocks[bnum]:
                rr = r + dr[d]
                cc = c + dc[d]
                if not (0<=rr<N) or not (0<=cc<M):
                    continue
                nbnum = board[rr][cc]
                if nbnum == 0:
                    continue
                if opposite[d] in blocks[nbnum]:
                    if (rr, cc) not in locs:
                        status.append((rr, cc))
        
        elapsed += 1
    
    print(f"#{t+1} {len(locs)}")

    