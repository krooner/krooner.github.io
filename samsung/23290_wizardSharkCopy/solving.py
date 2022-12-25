from copy import deepcopy
# 8가지의 방향
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

grid = {}
smells = {}

M, S = list(map(int, input().split()))
for _ in range(M):
    fr, fc, fd = list(map(int, input().split()))
    fr -= 1
    fc -= 1
    fd -= 1
    if (fr, fc) not in grid.keys():
        grid[(fr, fc)] = [fd]
    else:
        grid[(fr, fc)].append(fd)

sr, sc = list(map(int, input().split()))
sr -= 1
sc -= 1

new_grid = None

def move_fish():
    new_grid = {}
    for key, fish_dirs in grid.items():
        for fd in fish_dirs:
            i = 0
            for _ in range(8):
                nr = key[0] + dr[(fd-i)%8]
                nc = key[1] + dc[(fd-i)%8]
                flag = True
                # (nr, nc)가 상어 칸 이거나, 물고기 냄새 칸이거나, 격자 밖이라면 불가능.
                if (nr, nc) == (sr, sc): flag = False
                if (nr, nc) in smells.keys(): flag = False
                if nr <0 or nr >= 4 or nc < 0 or nc >= 4: flag = False
                if flag == True: # 불가능하므로 방향 변경 시작해야 함
                    if (nr, nc) not in new_grid:
                        new_grid[(nr, nc)] = [(fd-i)%8]
                    else:
                        new_grid[(nr, nc)].append((fd-i)%8)
                    break
                else:
                    i += 1
            if i == 8:
                if key not in new_grid:
                    new_grid[key] = [fd]
                else:
                    new_grid[key].append(fd)
    
    return new_grid
                

shark_r = [-1, 0, 1, 0]
shark_c = [0, -1, 0, 1]

candidates = []
visited = []

def move_shark(count, rr, cc, dirs, scores):
    # 현재 상어의 위치를 알고 상하좌우
    # (물고기 점수, 이동방향)
    global candidates, visited
    if count == 3: #세번 움직였으면 결과 반환
        candidates.append((scores, int(dirs)))
        return
    
    for i in range(4): # 현재 위치에서 상좌하우
        nr = rr + shark_r[i]
        nc = cc + shark_c[i]
        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4: # 새로운 위치가 격자 밖일 때 
            continue
        if (nr, nc) in visited: # 이미 방문한 곳일 때
            continue
        scores += len(new_grid[(nr, nc)]) if (nr, nc) in new_grid else 0 # 이동한 방향의 물고기 수를 현재 점수에서 추가함
        visited.append((nr, nc)) # 이동할 곳을 방문한 곳으로 기록함
        move_shark(count+1, nr, nc, dirs+str(i+1), scores) # 이동한 위치에서 다시 시도함
        visited.pop()
        scores -= len(new_grid[(nr, nc)]) if (nr, nc) in new_grid else 0
    
    return

def remove_smell(t): # 현재 - 과거
    global smells
    new_smells = {}
    for key, values in smells.items():
        update_values = [v for v in values if t - v < 2] # 냄새 생성씨기가
        if len(update_values) > 0:
            new_smells[key] = update_values
    
    smells = deepcopy(new_smells)
    return

def apply_copy():
    global new_grid
    for key, value in grid.items():
        if key in new_grid:
            new_grid[key] += value
        else:
            new_grid[key] = value
    
    return
        
for i in range(S): #magic repeat
    # copy_fish: grid
    new_grid = move_fish()

    visited = [(sr, sc)]
    move_shark(0, sr, sc, "", 0)
    
    candidates.sort(key = lambda x: (-x[0], x[1]))
    for item in list(str(candidates[0][1])):
        d = int(item) - 1
        sr += shark_r[d]
        sc += shark_c[d]
        # if len(new_grid[(sr, sc)]) > 0:
        if (sr, sc) in new_grid:
            new_grid[(sr, sc)] = []
            if (sr, sc) not in smells.keys():
                smells[(sr, sc)] = [i]
            else:
                smells[(sr, sc)].append(i)
    
    visited = []
    candidates = []
    
    remove_smell(i)
    apply_copy()
    
    grid = deepcopy(new_grid)
    new_grid = None
    
answer = 0
for values in grid.values():
    answer += len(values)

print(answer)
# 마법 순서
# 1. 물고기 복제 (초기 그리드 정보를 복제해 놓기)
# 2. 물고기 이동 (새 그리드에다가 이동한 물고기 정보 업데이트)
# 3. 상어의 이동 (큐를 활용해서 이동 가능 경우의 수를 적용하면서 잡은 물고기 수를 계산)
# (물고기수, 사전순 숫자) 를 고려한 소팅으로 적용한다
# 그리고 그 결정에 따른 물고기 냄새를 적용한다. (물고기 냄새가 연습 몇 회차인지 카운팅 필요하다)
# 4. 현재 기준 두번 전 연습에서 생긴 물고기 냄새를 제거한다.
# 5. 1.에서 복제한 결과가 적용된다.
