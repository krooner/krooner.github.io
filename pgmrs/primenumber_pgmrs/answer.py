from itertools import combinations
import math
test_cases = [[1,2,3,4],[1,2,7,6,4]]

for t in test_cases:
    answer=0
    l = [sum(picks) for picks in list(combinations(t, 3))]

    
    for number in l:
        prime_flag=True
        bound = int(math.sqrt(number))
        for divisor in range(2, bound+1):
            if number%divisor==0:
                prime_flag=False
                break
        if prime_flag:
            answer+=1
    
    print(answer)

    

