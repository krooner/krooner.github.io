import heapq
W, N = list(map(int, input().split()))

heap = []
for _ in range(N):
    w, p = list(map(int, input().split()))
    heapq.heappush(heap, [-p, w])

answer = 0
remain = W
for _ in range(len(heap)):
    # w, p = weight_prices[i]
    neg_p, w = heapq.heappop(heap)
    if remain == 0:
        break
    elif remain >= w:
        remain -= w
        answer += w*-neg_p
    else:
        answer += remain*-neg_p
        remain = 0

print(answer)