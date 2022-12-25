N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

order = ['L', 'D', 'R', 'U']

def check(new_coor):
    if 0>new_coor[0] or new_coor[0]>=N or 0>new_coor[1] or new_coor[1]>=N:
        return False
    else:
        return True

def move(y_coor, changed):
    garbage = 0

    r, c = y_coor
    y_sand = grid[r][c]
    left = grid[r][c]

    seven = int(y_sand*0.07)
    left -= 2*seven

    # 1UP seven
    new_coor = r+changed['U'][0], c+changed['U'][1]
    if not check(new_coor):
        garbage += seven
    else:
        grid[new_coor[0]][new_coor[1]]+=seven

    # 1DOWN seven
    new_coor = r+changed['D'][0], c+changed['D'][1]
    if not check(new_coor):
        garbage += seven
    else:
        grid[new_coor[0]][new_coor[1]]+=seven

    two = int(y_sand*0.02)
    left -= 2*two

    # 2UP two
    new_coor = r+2*changed['U'][0], c+2*changed['U'][1]
    if not check(new_coor):
        garbage += two
    else:
        grid[new_coor[0]][new_coor[1]]+=two

    # 2DOWN two
    new_coor = r+2*changed['D'][0], c+2*changed['D'][1]
    if not check(new_coor):
        garbage += two
    else:
        grid[new_coor[0]][new_coor[1]]+=two

    one = int(y_sand*0.01)
    left -= 2*one

    # 1U 1R one
    new_coor = r+changed['U'][0]+changed['R'][0], c+changed['U'][1]+changed['R'][1]
    if not check(new_coor):
        garbage += one
    else:
        grid[new_coor[0]][new_coor[1]]+=one
    # 1D 1R one
    new_coor = r+changed['D'][0]+changed['R'][0], c+changed['D'][1]+changed['R'][1]
    if not check(new_coor):
        garbage += one
    else:
        grid[new_coor[0]][new_coor[1]]+=one


    ten = int(y_sand*0.1)
    left -= 2*ten

    # 1U 1L ten
    new_coor = r+changed['U'][0]+changed['L'][0], c+changed['U'][1]+changed['L'][1]
    if not check(new_coor):
        garbage += ten
    else:
        grid[new_coor[0]][new_coor[1]]+=ten
    # 1D 1L ten
    new_coor = r+changed['D'][0]+changed['L'][0], c+changed['D'][1]+changed['L'][1]
    if not check(new_coor):
        garbage += ten
    else:
        grid[new_coor[0]][new_coor[1]]+=ten

    five = int(y_sand*0.05)
    left -= five

    # 2L five
    new_coor = r+2*changed['L'][0], c+2*changed['L'][1]
    if not check(new_coor):
        garbage += five
    else:
        grid[new_coor[0]][new_coor[1]]+=five

    # 1L left (y_sand)
    new_coor = r+changed['L'][0], c+changed['L'][1]
    if not check(new_coor):
        garbage += left
    else:
        grid[new_coor[0]][new_coor[1]]+=left

    grid[r][c]=0
    
    return garbage


idx = 0
repeat = 2*N-1

answer = 0

directions = {
    "L": (0, -1),
    "D": (1, 0),
    "R": (0, 1),
    "U": (-1, 0),
}

rotate = list("LURD")

start_idx = (int(N/2), int(N/2))
curr_idx = start_idx

for i in range(repeat): # 방향 변경 횟수
    idx = idx%4 # 방향 결정
    direct = order[idx] # 토네이도가 움직일 방향
    offset = rotate.index(direct) # 왼쪽 기준 회전해야할 횟수
    changed = {rotate[r]:directions[rotate[(r+offset)%4]] for r in range(len(rotate))}

    # direct = "L" -> (L U R D) (L U R D)
    # direct = "U" ->           (U R D L)
    # direct = "R" ->           (R D L U) 
    # direct = "D" ->           (D L U R)

    ## 마지막 고려해서 이동 횟수 결정
    length = int(1+i/2) if i!=repeat-1 else int(1+(i-1)/2)

    for j in range(length): # 특정 방향에서 이동 횟수 반복

        y_coor = (curr_idx[0]+directions[direct][0], curr_idx[1]+directions[direct][1]) # 이동할 좌표 결정, 한 칸씩 이동

        assert 0<=y_coor[0]<N
        assert 0<=y_coor[1]<N

        curr_idx = y_coor # 토네이도 이동 위치

        answer += move(y_coor, changed)

    idx += 1

assert curr_idx==(0, 0)

print(answer)

    