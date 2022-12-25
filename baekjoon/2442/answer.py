N = int(input())

for i in range(N):
    side_ = " "*(N-i-1)
    center = "*"*(2*i+1)
    print(side_+center)