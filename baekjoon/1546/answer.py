N = int(input())
l = list(map(int, input().split()))

assert N==len(l)

M = max(l)
new_scores = [(score/M)*100 for score in l]

print(sum(new_scores)/len(new_scores))