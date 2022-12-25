N, K = map(int, input().split())

l = [i for i in range(1, N+1)]
answer = []
curr = 0
while len(l)!=0:
    length = len(l)
    curr = (curr+K-1)%length
    answer.append(l[curr])
    l.remove(l[curr])
answer = str(answer)[1:-1]
print("<{}>".format(answer))
