from collections import deque

T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for t in range(T):
    N = int(input())
    atoms = deque([])
    for _ in range(N):
        info = list(map(int, input().split()))
        atoms.append(info)

    answer = 0

    while True:
        if len(atoms) == 0:
            break
        
        dict_ = {}

        for _ in range(len(atoms)):
            x, y, d, k = atoms.popleft()
            if abs(x)>1000 or abs(y)>1000:
                continue
            if (x, y) not in dict_:
                dict_[(x, y)] = [[d, k]]
            else:
                dict_[(x, y)].append([d, k])
        
        for key, value in dict_.items():
            if len(value) > 1:
                collision = sum([item[1] for item in value])
                answer += collision
            if len(value) == 1:
                d = value[0][0]
                x = key[0] + dx[d]*0.5
                y = key[1] + dy[d]*0.5
                atoms.append([x, y, value[0][0], value[0][1]])
    
    print(f"#{t+1} {answer}")