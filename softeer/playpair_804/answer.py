from collections import deque

alphabets = {chr(item): True for item in range(65, 91)}

msg = input()
key = list(input())

table = [None for _ in range(25)]

idx = 0
for c in key:
    if alphabets[c]:
        alphabets[c] = False
        table[idx] = c
        idx += 1


for num in range(65, 91):
    if num == 74:
        continue
    if idx == 25:
        break
    if alphabets[chr(num)]:
        table[idx] = chr(num)
        idx += 1

grid = [table[i:i+5] for i in range(0, 25, 5)]
char_pos = {}
for i in range(5):
    for j in range(5):
        c = grid[i][j]
        char_pos[c] = (i, j)
####

pairs = []
idx = 0
while True:

    division = [list(msg[i:i+2]) for i in range(0, len(msg), 2)]

    if len(division) == 0:
        break

    for item in division:
        if len(item) == 1:
            item.append('X')
            pairs.append(item.copy())
            idx += 2
        else:   
            a, b = item
            if a != b:
                pairs.append(item.copy())
                idx += 2
            else:
                remainder = msg[idx:]
                if a == 'X':
                    msg = "XQ" + remainder[1:]
                else:
                    msg = remainder[0] + "X" + remainder[1:]
                idx = 0
                break
    
    msg = msg[idx:]

####
answer = ""
for pair in pairs:
    lc, rc = pair
    lcr, lcc = char_pos[lc]
    rcr, rcc = char_pos[rc]

    after_lc = None
    after_rc = None
    if lcr == rcr:
        after_lc = grid[lcr][(lcc+1)%5]
        after_rc = grid[rcr][(rcc+1)%5]
    elif lcc == rcc:
        after_lc = grid[(lcr+1)%5][lcc]
        after_rc = grid[(rcr+1)%5][rcc]
    else:
        after_lc = grid[lcr][rcc]
        after_rc = grid[rcr][lcc]
    
    answer += after_lc
    answer += after_rc

print(answer)








        