# 8개 방향: 북 북동 동 ... 북서
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = list(map(int, input().split()))

grid = {}

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    r -= 1
    c -= 1
    key = (r, c)
    if key in grid:
        grid[key].append((m, s, d))
    else:
        grid[key] = [(m, s, d)]

for i in range(K):
    # 1. 모든 파이어볼이 d_i 방향으로 s_i 칸 만큼 이동
    new_grid = {}

    # 2. 이동 종류 후 2개 이상의 파이어볼이 있는 칸
    #   2-1. 하나로 합체
    #   2-2. 4개의 파이어볼로 분리
    #   2-3. 나뉜 파이어볼 (질량: 합//5), (속력: int(평균)), (방향: 모두 짝/홀: 0246 - Otherwise: 1357)
    #   2-4. 질량 0인 파이어볼 소멸