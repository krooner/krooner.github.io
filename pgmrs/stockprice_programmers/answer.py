test_cases = [
    [1,2,3,2,3]
]

for prices in test_cases:
    answer = []
    
    for i in range(len(prices)):
        flag=True
        for j in range(i+1, len(prices)):
            
            if prices[i] > prices[j]:
                answer.append(j-i)
                flag=False
                break
        if flag:
            answer.append(len(prices)-1-i)
    
    print(answer)