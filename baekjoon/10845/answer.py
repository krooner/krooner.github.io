from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input())

queue=[]

for _ in range(N):
    l = input().split()
    if len(l) != 1: # push
        element = int(l[1])
        queue.append(element)
    else:
        if l[0]=='pop':
            if len(queue)==0:
                print('-1\n')
            else:
                print(str(queue[0])+'\n')
                queue=queue[1:]
        elif l[0]=='size':
            print(str(len(queue))+'\n')
        elif l[0]=='empty':
            if len(queue)==0:
                print('1\n')
            else:
                print('0\n')
        elif l[0]=='front':
            if len(queue)==0:
                print('-1\n')
            else:
                print(str(queue[0])+'\n')
        elif l[0]=='back':
            if len(queue)==0:
                print('-1\n')
            else:
                print(str(queue[-1])+'\n')