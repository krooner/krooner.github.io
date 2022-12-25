N, M = list(map(int, input().split()))

length_speed = []
for _ in range(N):
    l, s = list(map(int, input().split()))
    for _ in range(l):
        length_speed.append(s)

tests = []
for _ in range(M):
    l, s = list(map(int, input().split()))
    # tests.append((l, s))
    for _ in range(l):
        tests.append(s)

assert len(length_speed) == 100
assert len(tests) == 100

answer = 0
for i in range(100):
    diff = max(0, tests[i] - length_speed[i])
    answer = max(diff, answer)

print(answer)

