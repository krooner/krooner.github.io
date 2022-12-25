N, M = list(map(int, input().split()))

rooms = {}
for _ in range(N):
    name = input()
    rooms[name] = [True for _ in range(9)]

for _ in range(M):
    name, s, t = input().split()
    s = int(s) - 9
    t = int(t) - 9
    for i in range(s, t):
        rooms[name][i] = False

empty = {}
for k in rooms:
    l = []
    start = None
    for i in range(len(rooms[k])):
        if rooms[k][i]:
            if start == None:
                start = i
        else:
            if start != None:
                a, b = str(start+9), str(i+9)
                if len(a) == 1:
                    a = "0"+a
                l.append((a, b))
                start = None
    if start != None:
        a, b = str(start+9), "18"
        if len(a) == 1:
            a = "0"+a
        l.append((a, b))
    empty[k] = l

for i, k in enumerate(sorted(empty.keys())):
    print(f"Room {k}:")
    if len(empty[k]) == 0:
        print("Not available")
    else:
        print(f"{len(empty[k])} available:")
        for a, b in empty[k]:
            print(f"{a}-{b}")
    if i != len(empty.keys())-1:
        print("-----")
