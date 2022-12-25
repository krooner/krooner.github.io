T = int(input())

for _ in range(T):
    n = int(input())
    l=[]
    while n!=0:
        l.append(n%2)
        n=int(n/2)
    answer = [str(i) for i, digit in enumerate(l) if digit==1]
    print(" ".join(answer))