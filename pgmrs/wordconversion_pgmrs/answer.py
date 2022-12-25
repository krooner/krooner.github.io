def recursion(word, idx, target, words, step, wordlist):
    if word==target:
        return step
    
    answer = 0
    alphabets = [w[idx] for w in words]
    
    for i in range(len(alphabets)):
        wordalphabets = list(word)
        wordalphabets[idx] = alphabets[i]
        newword = "".join(wordalphabets)
        
        if newword not in words or newword in wordlist:
            continue
        else:
            wordlist.append(newword)
            for j in range(len(word)):
                if idx==j:
                    continue
                result = recursion(newword, j, target, words, step+1, wordlist)
                if result!=0:
                    if answer==0:
                        answer = result
                    else:
                        answer = min(answer, result)
    return answer

def solution(begin, target, words):
    answer = 0
    
    for i in range(len(begin)):
        result = recursion(begin, i, target, words, 0, [begin])
        if result!=0:
            if answer==0:
                answer = result
            else:
                answer = min(answer, result)
            
    
    return answer