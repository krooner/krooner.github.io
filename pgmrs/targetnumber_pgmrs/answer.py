def recursion(numbers, mid, idx, target):
    if idx==len(numbers):
        if mid==target:
            return 1
        else:
            return 0
    
    return recursion(numbers, mid+numbers[idx], idx+1, target)+recursion(numbers, mid-numbers[idx], idx+1, target)
    
    
    

def solution(numbers, target):
    answer = recursion(numbers, 0, 0, target)
    
    return answer