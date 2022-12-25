from collections import defaultdict, deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

rules = {
    0: [2, 3], # 우 -> 상, 하
    1: [2, 3], # 좌 -> 상, 하
    2: [0, 1], # 상 -> 좌, 우
    3: [0, 1]  # 하 -> 좌, 우     
}

R, C, K = list(map(int, input().split()))

warmer = {}
observe = set()
for i in range(R):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if 1<=row[j]<=4:
            warmer[(i, j)] = row[j]-1
        if row[j] == 5:
            observe.add((i, j))

board = [[0 for _ in range(C)] for _ in range(R)]

walls = defaultdict(set)
W = int(input())
for _ in range(W):
    r, c, t = list(map(int, input().split()))
    r -= 1
    c -= 1
    if t == 0:
        a, b = (r, c), (r-1, c)
        walls[a].add(b)
        walls[b].add(a)
    else:
        a, b = (r, c), (r, c+1)
        walls[a].add(b)
        walls[b].add(a)

def candidates(pos, walls, rules, amount):
    '''
    A point -> expanded points
    '''
    answers = []
    r, c = pos
    rr, cc = r + dr[d], c + dc[d]
    if (rr, cc) not in walls[pos]:
        if 0<=rr<R and 0<=cc<C:
            answers.append((rr, cc, amount))
    for rule in rules[d]:
        rr, cc = r + dr[rule], c + dc[rule]
        rrr, ccc = rr + dr[d], cc + dc[d]
        if not (0<=rr<R) or not (0<=cc<C):
            continue
        if not (0<=rrr<R) or not (0<=ccc<C):
            continue
        if (rr, cc) not in walls[pos] and (rrr, ccc) not in walls[(rr, cc)]:
            answers.append((rrr, ccc, amount))
    
    return answers


def bfs(pos, d, amount, board):
    tasks = deque([])
    visited = set()
    inits = candidates(pos, walls, rules, amount)
    for item in inits:
        tasks.append(item)
    
    while len(tasks) != 0:
        # 1. check ele in deque

        for _ in range(len(tasks)):
            pr, pc, tmp = tasks.popleft()
            if tmp-1 > 0:
                # 2. add to deque
                next_candidates = candidates((pr, pc), walls, rules, tmp-1)
                for item in next_candidates:
                    tasks.append(item)
            if (pr, pc) not in visited:
                visited.add((pr, pc))
                board[pr][pc] += tmp


cnt = 0
while True:
    if cnt > 100:
        break
    # 1. warmer-work
    for wm in warmer:
        r, c = wm
        d = warmer[wm]
        rr, cc = r + dr[d], c+ dc[d]
        board[rr][cc] += 5
        bfs((rr, cc), d, 4, board)
    # 2. adjust temp
    exchange = defaultdict(list)
    for r in range(R):
        for c in range(C):
            center_tmp = board[r][c]
            for m in range(4):
                rr, cc = r + dr[m], c + dc[m]
                if not (0<=rr<R) or not (0<=cc<C):
                    continue
                if (rr, cc) in walls[(r, c)]:
                    continue
                counter_tmp = board[rr][cc]
                if center_tmp < counter_tmp:
                    q = (counter_tmp - center_tmp)//4
                    exchange[(r, c)].append(q)
                    exchange[(rr, cc)].append(-q)
    
    for k, v in exchange.items():
        r, c = k
        board[r][c] += sum(v)

    # 3. reduce outdoor temp by 1 whose curr temp >= 1
    left = [board[i][0] for i in range(R)]
    right = [board[i][-1] for i in range(R)]
    for i in range(R):
        if left[i] >= 1:
            board[i][0] -= 1
        if right[i] >= 1:
            board[i][-1] -= 1
        
    top = [board[0][i] for i in range(1, C-1)]
    bottom = [board[-1][i] for i in range(1, C-1)]
    for i in range(len(top)):
        if top[i] >= 1:
            board[0][1+i] -= 1
        if bottom[i] >= 1:
            board[-1][1+i] -= 1

    # 4. plus cnt
    cnt += 1

    # 5. investigation
    test_flag = True
    for item in observe:
        r, c = item
        if board[r][c] < K:
            test_flag = False
            break
    if test_flag:
        break

if cnt > 100:
    print(101)
else:
    print(cnt)
