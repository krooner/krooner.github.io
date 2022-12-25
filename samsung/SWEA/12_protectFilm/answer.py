from itertools import combinations, product

T = int(input())

def function(bd, D, W, K):
    for p in range(K):
        for item in combinations([i for i in range(D)], p):
            for choose in product("01", repeat=len(item)):
                cmds = {item[i]: int(choose[i]) for i in range(len(item))}
                for col in range(W):
                    for crit in range(D-K+1):
                        feat = cmds[crit] if crit in cmds else bd[crit][col] 
                        for dr in range(1, K):
                            counter = cmds[crit+dr] if crit+dr in cmds else bd[crit+dr][col]
                            if feat != counter:
                                break
                        else:
                            break
                    else:
                        break
                else:
                    return p
    return K

for t in range(T):
    D, W, K = list(map(int, input().split()))

    board = []
    for _ in range(D):
        row = list(map(int, input().split()))
        board.append(row)
    
    answer = function(board, D, W, K)

    print(f"#{t+1} {answer}") 