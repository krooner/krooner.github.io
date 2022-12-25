N = int(input())

for _ in range(N):
    words = input().split()
    rwords = []
    for word in words:
        word = list(word)
        word.reverse()
        rwords.append("".join(word))
    print(" ".join(rwords))