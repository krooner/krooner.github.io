N = int(input())
l = list(map(int, input().split()))

assert N==len(l)

l = sorted(l)
print(l[0]*l[-1])