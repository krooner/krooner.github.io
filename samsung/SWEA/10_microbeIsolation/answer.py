from collections import defaultdict

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
opposite = {0:1, 1:0, 2:3, 3:2}

T = int(input())

for t in range(T):
    N, M, K = list(map(int, input().split()))

    dict_ = defaultdict(list)

    for _ in range(K):
        r, c, count, d = list(map(int, input().split()))
        dict_[(r, c)].append([count, d-1])
    
    for _ in range(M):
        move_ = defaultdict(list)
        for key, value in dict_.items():
            r, c = key
            count, d = value[0]

            r += dr[d]
            c += dc[d]

            if not (0<r<N-1) or not (0<c<N-1):
                count = int(count/2)
                d = opposite[d]
                if count == 0:
                    continue
            move_[(r, c)].append([count, d])
        
        for key in move_.keys():
            l = move_[key]
            l.sort(key = lambda x: x[0], reverse=True)
            d = l[0][1]
            count = sum([item[0] for item in l])
            move_[key] = [[count, d]]
        
        dict_ = move_
    
    answer = sum([value[0][0] for value in dict_.values()])

    print(f"#{t+1} {answer}")

