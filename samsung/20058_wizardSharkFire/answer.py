dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, Q = list(map(int, input().split()))
big_len = pow(2, N)
A = []
for _ in range(big_len):
    row = list(map(int, input().split()))
    A.append(row)
L = list(map(int, input().split()))

# 1) 부분격자를 시계방향 90도 회전
# 2) 인접한 4칸 중, 얼음이 있는 칸이 2칸 이하인 경우 얼음의 양 1 차감
for q in range(Q):
    part_len = pow(2, L[q])
    B = [[0 for _ in range(big_len)] for _ in range(big_len)]
    if part_len > 1:
        for r in range(0, big_len, part_len):
            for c in range(0, big_len, part_len):

                for a in range(part_len): # row
                    for b in range(part_len):
                        curr_r = r+a
                        curr_c = c+b

                        rotate_r = r+b
                        rotate_c = c+part_len-1-a

                        B[rotate_r][rotate_c] = A[curr_r][curr_c]
    
    for r in range(big_len):
        for c in range(big_len):
            count = 0

            for k in range(4):
                rr = r + dr[k]
                cc = c + dc[k]
                if rr < 0 or rr >= big_len or cc < 0 or cc >= big_len:
                    continue
                if B[rr][cc] == 0:
                    continue
                count += 1
            
            if count >= 3 or B[r][c] == 0:
                continue
            else:
                B[r][c] -= 1


    # A = deepcopy(B)
    A = B

# from collections import deque

ice_sum = 0
for r in range(big_len):
    for c in range(big_len):
        if A[r][c] > 0:
            ice_sum += A[r][c]

max_counts = 0
for r in range(big_len):
    for c in range(big_len):
        if A[r][c] > 0:
            counts = 1
            dq = [(r, c)]
            A[r][c] = -1
            while True:
                if len(dq) == 0:
                    break
                for _ in range(len(dq)):
                    pr, pc = dq.pop()
                    
                    for i in range(4):
                        rr = pr + dr[i]
                        cc = pc + dc[i]

                        if rr < 0 or rr >= big_len or cc < 0 or cc >= big_len:
                            continue
                        if A[rr][cc] > 0:
                            counts += 1
                            A[rr][cc] = -1
                            dq.append((rr, cc))
            
            max_counts = max(counts, max_counts)

print(ice_sum)
print(max_counts)