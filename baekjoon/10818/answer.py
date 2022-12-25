N = int(input())
l = list(map(int, input().split()))

assert N==len(l)

print("{} {}".format(min(l), max(l)))