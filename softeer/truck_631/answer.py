N = int(input())

users = {}

for i in range(N):
    _, *L = list(map(int, input().split()))
    L = [L[i:i+2] for i in range(0, len(L), 2)]
    print(L)

M = int(input())
scenarios = list(map(int, input().split()))

