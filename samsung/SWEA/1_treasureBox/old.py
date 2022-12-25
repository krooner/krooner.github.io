T = int(input())

symbols = list('0123456789ABCDEF')
convert = {item: i for i, item in enumerate(symbols)}

for t in range(T):
    N, K = list(map(int, input().split()))
    numlist = list(input())

    q, _ = divmod(N, 4)

    edgenumset = set()
    for i in range(q): # rotation
        for j in range(0, N, q): # each edge
            edgenum = 0
            for a in range(q): # element in edge
                symbol = numlist[(i+j+a)%N]
                num = convert[symbol]
                edgenum += pow(16, q-a-1)*num
            edgenumset.add(edgenum)
    
    edgenumbers = sorted(edgenumset, reverse=True)
    answer = edgenumbers[K-1]

    print(f'#{t+1} {answer}')