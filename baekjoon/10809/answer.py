word = list(input())

# ord('a') = 97
# ord('z') = 122
alphabets=[chr(i) for i in range(97, 123)]
l=['-1' for _ in range(26)]

for i, a in enumerate(word):
    if l[alphabets.index(a)]=='-1':
        l[alphabets.index(a)]=str(i)

print(" ".join(l))