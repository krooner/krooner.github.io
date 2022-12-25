N, M = list(map(int, input().split()))

dr = [-1, 1, 0, 0]; dc = [0, 0, -1, 1]
rdr = [0, 1, 0, -1]; rdc = [-1, 0, 1, 0]

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

magics = []
for _ in range(M):
    d, s = list(map(int, input().split()))
    d -= 1
    magics.append((d, s))

sr, sc = int(N/2), int(N/2)

total_info = {item: 0 for item in range(1, 4)}

def explode(beads):
    consec, num = None, None
    skip_indices = []
    for i in range(len(beads)):
        if i == 0:
            consec = 1; num = beads[i]
        else:
            if num == beads[i]: # curr one = prev one
                consec += 1
            else: # curr one != prev one
                if consec >= 4:
                    skip_indices += [i-1-j for j in range(consec)]
                consec = 1; num = beads[i]
        if i == len(beads)-1:
            if consec >= 4:
                skip_indices += [i-j for j in range(consec)]
    
    for i in skip_indices:
        total_info[beads[i]] += 1

    answer = [beads[i] for i in range(len(beads)) if i not in skip_indices]
    return answer

def get_beads(board): # 1 - 1 - 2 - 2 - 3 - 3 - 4 - 4, ...
    move = 1
    cr, cc, cd = sr, sc, 0
    beads = []
    while True:
        for _ in range(2): # repeat two
            for _ in range(move):
                cr += rdr[cd]; cc += rdc[cd]
                if not (0<=cr<N) or not (0<=cc<N):
                    return beads
                if board[cr][cc] != 0:
                    beads.append(board[cr][cc])
            cd = (cd+1)%4
        move += 1

def rearrange(board, new_beads):
    move = 1
    cr, cc, cd = sr, sc, 0
    idx = 0
    while True:
        for _ in range(2): # repeat two
            for _ in range(move): 
                cr += rdr[cd]; cc += rdc[cd]
                if not (0<=cr<N) or not (0<=cc<N) or idx == len(new_beads):
                    return 
                board[cr][cc] = new_beads[idx]
                idx += 1
            cd = (cd+1)%4
        move += 1
    
def change_beads(beads):
    group, num = None, None
    new_beads = []
    for i in range(len(beads)):
        if i == 0:
            group = 1
            num = beads[i]
            continue
        else:
            if num == beads[i]:
                group += 1
            else:
                beadA, beadB = group, num
                new_beads += [beadA, beadB]
                group = 1
                num = beads[i]
        if i == len(beads)-1:
            if group > 0:
                beadA, beadB = group, num
                new_beads += [beadA, beadB]
    
    return new_beads


def update(board):
    beads = get_beads(board)
    # print(beads)
    # print()

    while True:
        output = explode(beads)
        if len(beads) == len(output):
            break
        beads = output
    # print(beads)
    # print()

    new_beads = change_beads(beads)
    # print(new_beads)
    # print()

    for i in range(N):
        for j in range(N):
            board[i][j] = 0

    rearrange(board, new_beads)

for magic in magics:
    d, s = magic
    for i in range(1, s+1):
        rr, cc = sr + i*dr[d], sc + i*dc[d]
        board[rr][cc] = 0

    update(board)
    # print(board)


answer = 0
for k, v in total_info.items():
    answer += k*v
print(answer)