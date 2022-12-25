test_cases = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [4,2,0,3,2,5]
]

for height in test_cases:

    max_ = max(height)
            
    sum_=0
    for idx in range(1, max_+1):
        boundaries=[i for i in range(len(height)) if height[i]>=idx]
        if len(boundaries)>1:
            for i in range(len(boundaries)-1):
                sum_+=boundaries[i+1]-boundaries[i]-1

    print(sum_)