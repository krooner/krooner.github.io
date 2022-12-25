from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input())

deque=[]

for _ in range(N):
    l = input().split()
    if len(l) != 1: # push
        element = int(l[1])
        if l[0]=='push_back':
            deque.append(element)    
        elif l[0]=='push_front':
            deque = [element]+deque
    else:
        if l[0]=='pop_front':
            if len(deque)==0:
                print('-1\n')
            else:
                print(str(deque[0])+'\n')
                deque=deque[1:]
        elif l[0]=='pop_back':
            if len(deque)==0:
                print('-1\n')
            else:
                print(str(deque[-1])+'\n')
                deque=deque[:-1]
        elif l[0]=='size':
            print(str(len(deque))+'\n')
        elif l[0]=='empty':
            if len(deque)==0:
                print('1\n')
            else:
                print('0\n')
        elif l[0]=='front':
            if len(deque)==0:
                print('-1\n')
            else:
                print(str(deque[0])+'\n')
        elif l[0]=='back':
            if len(deque)==0:
                print('-1\n')
            else:
                print(str(deque[-1])+'\n')