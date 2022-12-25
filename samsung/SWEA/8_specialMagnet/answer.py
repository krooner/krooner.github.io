from collections import deque

T = int(input())
for t in range(T):
    K = int(input())

    magnets = {}
    for i in range(4):
        m = list(map(int, input().split()))
        magnets[i] = deque(m)
    
    for _ in range(K):
        midx, direct = list(map(int, input().split()))
        midx -= 1
        others = [[midx, direct]]

        curr, curr_dir = midx, direct
        left = midx-1
        while left >= 0:
            curr_m = magnets[curr]
            left_m = magnets[left]

            if curr_m[6] != left_m[2]:
                curr_dir *= -1
                others.append([left, curr_dir])
            else:
                break

            curr -= 1
            left -= 1
        
        curr, curr_dir = midx, direct
        right = midx+1

        while right < 4:
            curr_m = magnets[curr]
            right_m = magnets[right]

            if curr_m[2] != right_m[6]:
                curr_dir *= -1
                others.append([right, curr_dir])
            else:
                break

            curr += 1
            right += 1

        for idx, d in others:
            if d == 1: # clockwise
                ele = magnets[idx].pop()
                magnets[idx].appendleft(ele)
            else:
                ele = magnets[idx].popleft()
                magnets[idx].append(ele)
        
        print(others)

    answer = 0
    for i, v in enumerate(magnets.values()):
        if v[0] == 1:
            answer += pow(2, i)

    print(f"#{t+1} {answer}")