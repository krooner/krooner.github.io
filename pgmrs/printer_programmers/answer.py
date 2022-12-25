test_cases=[
    ([2,1,3,2], 2),
    ([1,1,9,1,1,1], 0)
]

for t in test_cases:
    answer = 0
    priorities, location = t

    l = [(item, i) for i, item in enumerate(priorities)]
    cnt = 1
    while len(l)!=0:
        front, loc = l[0]
        if len(l)==1 or front>=max([item for item, _ in l[1:]]):
            if loc == location:
                print(cnt)
            l = l[1:]
            cnt+=1
        else:
            l.append(l[0])
            l = l[1:]
            