def recursion(route, indices, tickets):
    if len(indices)==len(tickets):
        return route
    
    prev = ""
    answer = []
    for i in range(len(tickets)):
        if i in indices:
            continue
        if route[-1]==tickets[i][0]: # current destine = ticket depart
            result = recursion(route+[tickets[i][1]], indices+[i], tickets)
            if len(result)!=0:
                if len(prev)==0:
                    prev = "".join(result)
                    answer = result
                else:
                    if prev>"".join(result):
                        prev = "".join(result)
                        answer = result
    
    if len(answer)!=len(tickets)+1:
        return []
    return answer
    

def solution(tickets):
    answer = []
    
    prev = ""
    for i in range(len(tickets)):
        if tickets[i][0]=="ICN":
            result = recursion([tickets[i][0], tickets[i][1]], [i], tickets)
            if len(result)!=0:
                if len(prev)==0:
                    prev = "".join(result)
                    answer = result
                else:
                    if prev>"".join(result):
                        prev = "".join(result)
                        answer = result
        
    
    
    
    return answer