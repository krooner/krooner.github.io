N = int(input())

for _ in range(N):

    left = []
    ps = list(input())
    flag = True
    for p in ps:
        if p=='(':
            left.append(p)
        else: # ')'
            if len(left)!=0:
                left = left[:-1]
            else:
                flag = False
                break
    if len(left)!=0:
        flag = False
    
    print('YES' if flag else 'NO')
