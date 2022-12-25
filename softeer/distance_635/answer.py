import sys
sys.setrecursionlimit(10**6)

def dfs(current, parent):
    st_size[current] = 1
    for i in range(len(node[current])):
        child, weight = node[current][i]
        if child != parent:
            dfs(child, current)
            dist_sum[current] += dist_sum[child] + st_size[child] * weight
            st_size[current] += st_size[child]

    return

def move(current, parent):
    for i in range(len(node[current])):
        child, weight = node[current][i]
        if child != parent:
            dist_sum[child] = dist_sum[current] + weight*(N-2*st_size[child])
            move(child, current)
    
    return

N = int(input())

node = [[] for _ in range(N+1)]
st_size = [0] * (N+1)
dist_sum = [0] * (N+1)

for i in range(N-1):
    x, y, t = list(map(int, input().split()))
    node[x].append([y, t])
    node[y].append([x, t])

dfs(1, 1)
move(1, 1)

for i in range(len(dist_sum)):
    if i != 0:
        print(dist_sum[i])