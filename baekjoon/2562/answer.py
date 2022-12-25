# from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write
## IO Acceleration (print only str param)

l = [int(input()) for _ in range(9)]

maxval = max(l)
maxidx = l.index(maxval)

print(maxval)
print(maxidx+1)