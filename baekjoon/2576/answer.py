l = [int(input()) for _ in range(7)]

l = [num for num in l if num%2==1]

if len(l)==0:
    print(-1)
else:
    print(sum(l))
    print(min(l))