def included(idx, computers, flags, dig):

    for i in range(len(computers[idx])):
        if computers[idx][i]==1 and flags[idx][i]:
            dig = True
            flags[idx][i]=False
            if idx==i:
                continue
            dig, flags = included(i, computers, flags, dig)
    
    if dig:
        return True, flags
    else:
        return False, flags
    
        
                
            
    
    
    

def solution(n, computers):
    answer = 0
    flags = [[True for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        flag, flags = included(i, computers, flags, False)
        
        if flag:
            answer+=1

    
    return answer