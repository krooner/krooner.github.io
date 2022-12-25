test_cases = [
    (2, 10, [7, 4, 5, 6]),
    (100, 100, [10]),
    (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])    
]

for t in test_cases:
    cnt=0
    length, weight, trucks = t
    queue = []

    # 1. pop queue if timeout
    # 2. push queue as much as possible
    # 3. update count

    while len(trucks)!=0 or len(queue)!=0:
        cnt+=1
        left = queue.copy()
        for truck, distance in left:
            if distance==0:
                queue=queue[1:]
        
        curr_weight=sum([t for t, d in queue])

        if len(trucks)!=0 and len(queue)<length:
            if curr_weight+trucks[0]<=weight and len(queue)<length:
                queue.append((trucks[0], length))
                curr_weight=sum([t for t, d in queue])
                trucks=trucks[1:]

        queue = [(a, b-1) for a, b in queue]
        # print(cnt, queue)
    
    # break
        
        
        
    print(cnt)






