N = int(input())

def lineprint(num, N):
    if num==N:
        print("*"*(2*N-1))
        return

    side_ = " "*(N-num)
    center_ = "*"*(2*num-1)

    print(side_+center_)
    lineprint(num+1, N)
    print(side_+center_)

lineprint(1, N)