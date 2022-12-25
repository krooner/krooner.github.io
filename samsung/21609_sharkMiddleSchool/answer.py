from collections import deque
N, M = list(map(int, input().split()))

dr = [-1, 0, 1, 0]; dc = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(N)]

def expand_block_group(board, pos, remove=False):
    visited = {pos}
    blocks = {pos}
    checker = deque([pos])
    rainbow = 0
    area = 0
    while len(checker) > 0:
        for _ in range(len(checker)):
            br, bc = checker.popleft()
            if board[br][bc] == 0:
                rainbow += 1
            else:
                blocks.add((br, bc))
            area += 1
            for i in range(4):
                brr, bcc = br + dr[i], bc + dc[i]
                if not (0<=brr<N) or not (0<=bcc<N):
                    continue
                if board[brr][bcc] != board[pos[0]][pos[1]] and board[brr][bcc] != 0:
                    continue
                if (brr, bcc) not in visited:
                    visited.add((brr, bcc))
                    checker.append((brr, bcc))

    if remove:
        for item in visited:
            r, c = item
            board[r][c] = -2

    criterion = sorted(list(blocks), key = lambda x: (x[0], x[1]))[0]

    return area, rainbow, criterion

def find_block_group(board, N):
    # find block group
    answer = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                res_area, rainbow, criterion = expand_block_group(board, (i, j), remove=False)
                if res_area > 1:
                    cr, cc = criterion
                    answer.append((cr, cc, res_area, rainbow))

    return answer

def apply_gravity(board, N):
    for c in range(N):
        cnt = 0
        for r in range(N-1, -1, -1):
            if board[r][c] == -2:
                cnt += 1
            elif board[r][c] == -1:
                cnt = 0
            else:
                if cnt != 0:
                    board[r+cnt][c] = board[r][c]
                    board[r][c] = -2

    return board

def rotation(board, N):
    backup = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            backup[N - 1 - c][r] = board[r][c]

    for r in range(N):
        for c in range(N):
            board[r][c] = backup[r][c]

    return board

points = 0
while True:
    groups = find_block_group(board, N)
    if len(groups) == 0:
        break
    groups.sort(key = lambda x: (-x[2], -x[3], -x[0], -x[1]))
    br, bc, B, _ = groups[0]
    expand_block_group(board, (br, bc), remove=True)
    points += B*B

    # gravity
    board = apply_gravity(board, N)
    # rotate
    board = rotation(board, N)
    # gravity
    board = apply_gravity(board, N)

print(points)