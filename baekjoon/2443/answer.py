N = int(input())

for i in range(N):
    side_ = " "*i
    center_ = "*"*(2*(N-i)-1)
    print(side_+center_)