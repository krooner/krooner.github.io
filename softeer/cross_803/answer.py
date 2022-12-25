from collections import deque

N = int(input())

right = {
    "A": "D",
    "B": "A",
    "C": "B",
    "D": "C"
}

roads = {item : deque([]) for item in "ABCD"}


start_time = 0
for i in range(N):
    t, w = input().split()
    roads[w].append((i, int(t)))
    if i == 0:
        start_time = int(t)

logs = [-1 for _ in range(N)]
curr = start_time
while sum([len(roads[item]) for item in "ABCD"]) != 0:

    front_times = {item: 1e10 for item in "ABCD"}
    for item in "ABCD":
        if len(roads[item]) != 0:
            front_times[item] = roads[item][0][1]
    
    if min(front_times.values()) >= curr:
        curr = min(front_times.values())
    
    moveable = {item: False for item in "ABCD"}
    stuck = {item: False for item in "ABCD"}

    for item in "ABCD":
        right_side = right[item]
        if len(roads[item]) != 0: # something inside
            if len(roads[right_side]) == 0 and roads[item][0][1] <= curr:
                moveable[item] = True
            elif len(roads[right_side]) != 0 and roads[right_side][0][1] > curr and roads[item][0][1] <= curr: # empty or curr
                moveable[item] = True
            elif moveable[item] == False and roads[item][0][1] <= curr:
                stuck[item] = True
    
    if sum(stuck.values()) == 4:
        break

    for item, flag in moveable.items():
        if flag:
            i, _ = roads[item].popleft()
            logs[i] = curr
    
    curr += 1

for item in logs:
    print(item)