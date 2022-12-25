T = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for t in range(T):
    M, A = list(map(int, input().split()))
    moveinfo1 = list(map(int, input().split()))
    moveinfo2 = list(map(int, input().split()))
    
    pos1 = [1, 1]
    pos2 = [10, 10]

    ap_info = []
    for _ in range(A):
        ap = list(map(int, input().split()))
        ap_info.append(ap)

    answer = 0
    for i in range(M+1):
        # Check whether they're in AP coverage
        a_P = []
        b_P = []
        for j, item in enumerate(ap_info):
            ax, ay, c, p = item
            x1, y1 = pos1
            x2, y2 = pos2
            d1 = abs(x1-ax)+abs(y1-ay)
            d2 = abs(x2-ax)+abs(y2-ay)
            if c>=d1: a_P.append(j)
            if c>=d2: b_P.append(j)
        
        # TODO: Find max charge amount
        charge = 0

        if len(a_P) != 0 and len(b_P) == 0:
            charge = max([ap_info[item][-1] for item in a_P])
        elif len(a_P) == 0 and len(b_P) != 0:
            charge = max([ap_info[item][-1] for item in b_P])
        elif len(a_P) != 0 and len(b_P) != 0:
            for item1 in a_P:
                for item2 in b_P:
                    if item1 == item2:
                        a_charge = ap_info[item1][-1]/2
                        b_charge = ap_info[item2][-1]/2
                        charge = max(charge, a_charge+b_charge)
                    else:
                        a_charge = ap_info[item1][-1]
                        b_charge = ap_info[item2][-1]
                        charge = max(charge, a_charge+b_charge)

        answer += charge

        # update positions
        if i != M:
            movedir1, movedir2 = moveinfo1[i]-1, moveinfo2[i]-1
            if movedir1 != -1:
                pos1[0] += dx[movedir1]
                pos1[1] += dy[movedir1]
            if movedir2 != -1:
                pos2[0] += dx[movedir2]
                pos2[1] += dy[movedir2]
        
    print(f"#{t+1} {int(answer)}")