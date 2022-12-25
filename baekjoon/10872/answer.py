N = int(input())

ans=1
for num in range(N, 0, -1):
    ans*=num
print(ans)