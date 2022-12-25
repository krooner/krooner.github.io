T = int(input())

table = {
    "0": [1, 1, 1, 0, 1, 1, 1],
    "1": [0, 0, 1, 0, 0, 0, 1],
    "2": [0, 1, 1, 1, 1, 1, 0],
    "3": [0, 1, 1, 1, 0, 1, 1],
    "4": [1, 0, 1, 1, 0, 0, 1],
    "5": [1, 1, 0, 1, 0, 1, 1],
    "6": [1, 1, 0, 1, 1, 1, 1],
    "7": [1, 1, 1, 0, 0, 0, 1],
    "8": [1 for _ in range(7)],
    "9": [1, 1, 1, 1, 0, 1, 1],
    "A": [0 for _ in range(7)]
}


for _ in range(T):
    a, b = input().split()
    max_len = max(len(a), len(b))
    for _ in range(max_len - len(a)):
        a = "A"+a
    for _ in range(max_len - len(b)):
        b = "A"+b
    a, b = list(a), list(b)
    assert len(a) == len(b)

    answer = 0
    for i in range(max_len):
        bill_a = table[a[i]]
        bill_b = table[b[i]]

        answer += sum([abs(bill_a[j]-bill_b[j]) for j in range(7)])
    print(answer)


