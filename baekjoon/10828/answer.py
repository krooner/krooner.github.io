from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input())

stack=[]

for _ in range(N):
    l = input().split()
    if len(l) != 1: # push
        element = int(l[1])
        stack.append(element)
    else:
        if l[0]=='pop':
            if len(stack)==0:
                print('-1\n')
            else:
                print(str(stack[-1])+'\n')
                stack=stack[:-1]
        elif l[0]=='size':
            print(str(len(stack))+'\n')
        elif l[0]=='empty':
            if len(stack)==0:
                print('1\n')
            else:
                print('0\n')
        elif l[0]=='top':
            if len(stack)==0:
                print('-1\n')
            else:
                print(str(stack[-1])+'\n')