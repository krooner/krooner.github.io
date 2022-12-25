T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # _, location
    ll = list(map(int, input().split())) # priorities

    assert N==len(ll)

    l = [(item, i) for i, item in enumerate(ll)]
    order = 1
    while len(l)!=0:
        importance, loc = l[0]
        if len(l)==1 or importance>=max([item for item, _ in l[1:]]):
            if M == loc:
                print(order)
            l = l[1:]
            order+=1
        else:
            l.append(l[0])
            l=l[1:]
            


