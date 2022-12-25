test_cases = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]

for t in test_cases:
    origin = t
    # step 1.
    t = t.lower()
    # print(origin, t)

    # step 2.
    excludechars = [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(0, 10)] + ['-', '_', '.']
    t = [c for c in list(t) if c in excludechars]
    # print(t)

    # step 3.
    l = []
    consecutive=False
    for c in t:
        if c=='.':
            if not consecutive:
                consecutive=True
        else:
            if consecutive:
                consecutive=False
                l.append('.')
                l.append(c)
            else:
                l.append(c)
    # print(l)

    # step 4.
    if len(l)!=0:
        if l[0]=='.':
            l=l[1:]
        if l[-1]=='.':
            l=l[:-1]

    # step 5.
    if len(l)==0:
        l.append('a')
    
    # step 6.
    if len(l)>=16:
        l=l[:15]
        if l[-1]=='.':
            l=l[:-1]
    
    # step 7.
    if len(l)<=2:
        while len(l)!=3:
            l.append(l[-1])
    
    print("".join(l))