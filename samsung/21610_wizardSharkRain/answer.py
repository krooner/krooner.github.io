N, M = list(map(int, input().split()))

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

skills = []
for _ in range(M):
    d, s = list(map(int, input().split()))
    skills.append((d-1, s))

clouds = {(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)}
for skill in skills:
    d, s = skill
    move_clouds = set()
    for cloud in clouds:
        cr, cc = cloud
        cr = (cr + s*dr[d] + N) % N
        cc = (cc + s*dc[d] + N) % N
        board[cr][cc] += 1
        move_clouds.add((cr, cc))
    clouds = move_clouds
    del move_clouds
    bug_results = []
    for bp in clouds:
        br, bc = bp
        cnt = 0
        for i in [1, 3, 5, 7]:
            brr, bcc = br + dr[i], bc + dc[i]
            if 0<=brr<N and 0<=bcc<N and board[brr][bcc] > 0:
                cnt += 1
        if cnt > 0:
            bug_results.append((br, bc, cnt))
    for br, bc, cnt in bug_results:
        board[br][bc] += cnt

    new_clouds = set()
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i, j) not in clouds:
                new_clouds.add((i, j))
                board[i][j] -= 2

    clouds = new_clouds
    del new_clouds

answer = 0
for i in range(N):
    for j in range(N):
        answer += board[i][j]

print(answer)