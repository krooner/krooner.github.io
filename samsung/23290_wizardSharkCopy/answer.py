dr = [0, -1, -1, -1, 0, 1, 1, 1]; dc = [-1, -1, 0, 1, 1, 1, 0, -1]
sdr = [-1, 0, 1, 0]; sdc = [0, -1, 0, 1]

M, S = list(map(int, input().split()))

fishes = {}; smells = {}
for _ in range(M):
    r, c, d = list(map(int, input().split()))
    r -= 1; c -= 1; d -= 1
    key = (r, c)
    if key not in fishes:
        fishes[key] = [d]
    else:
        fishes[key].append(d)

sr, sc = list(map(int, input().split()))
sr -= 1; sc -= 1

def dfs(pos, num, routes, visited, ffishes):
    if len(routes) == 3:
        result = (num, int(routes))
        return [result]
    
    answers = []
    pr, pc = pos
    for i in range(4):
        rr, cc = pr + sdr[i], pc + sdc[i]
        key = (rr, cc)
        if 0<=rr<4 and 0<=cc<4 and key not in visited:
            fs = 0 if key not in ffishes else len(ffishes[key])
            visited.add(key)
            answers += dfs(key, num+fs, routes+str(i+1), visited, ffishes)
            visited.remove(key)
    
    return answers

cnt = 0
while cnt != S:
    # 1. start copy

    # 2. move fishes
    new_fishes = {}
    for pos, v in fishes.items():
        pr, pc = pos
        for d in v:
            original_d = d
            while True:
                rr, cc = pr + dr[d], pc + dc[d]
                moveable = True
                if not (0<=rr<4) or not (0<=cc<4):
                    moveable = False
                if (rr, cc) == (sr, sc) or (rr, cc) in smells:
                    moveable = False
                if moveable:
                    key = (rr, cc)
                    if key in new_fishes:
                        new_fishes[key].append(d)
                    else:
                        new_fishes[key] = [d]
                    break
                else:
                    d = (d+7)%8
                    if d == original_d:
                        key = (pr, pc)
                        if key in new_fishes:
                            new_fishes[key].append(d)
                        else:
                            new_fishes[key] = [d]
                        break
    
    # 3. move shark
    visited = set([(sr, sc)])
    possible = dfs((sr, sc), 0, "", visited, new_fishes)
    possible.sort(key=lambda x: (-x[0], x[1]))
    dirstring = possible[0][-1]
    print(dirstring)
    for c in str(dirstring):
        d = int(c)-1
        sr += sdr[d]; sc += sdc[d]; key = (sr, sc)
        if key in new_fishes:
            smells[key] = cnt
            del new_fishes[key]
    
    # 4. update smell
    keys = list(smells.keys())
    for k in keys:
        if cnt - smells[k] == 2:
            del smells[k]
    
    # 5. complete copy
    for k, v in fishes.items():
        if k in new_fishes:
            new_fishes[k] += fishes[k]
        else:
            new_fishes[k] = fishes[k]

    fishes = new_fishes
    cnt += 1

numfish = sum([len(v) for v in fishes.values()])

print(numfish)