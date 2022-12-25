def to_decimal(string):
    answer = 0
    for i in range(len(string)):
        asc_num = ord(string[len(string)-i-1])
        if asc_num >= 65:
            answer += (asc_num - 55) * pow(16, i)
        else:
            answer += (asc_num - 48) * pow(16, i)
    return answer

T = int(input())
for i in range(T):
    N, K = list(map(int, input().split()))
    values = list(input())
    # 회전: N/4번
    rep = N//4; print(rep)
    valueset = set()
    for j in range(rep):
        end = values[-1]
        values.pop()
        values.insert(0, end)
        for k in range(0, N, rep):
            decimal_value = to_decimal(values[k:k+rep])
            valueset.add(decimal_value)

    answer = sorted(valueset, reverse=True)[K-1]
    print(f"#{i+1} {answer}")
