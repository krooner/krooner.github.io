word = list(input())

# ord(A) = 65 -> 65 + 0
# ord(Z) = 90 -> 65 + 25

l_ = [chr(ord(alphabet)+23) if (ord(alphabet)-ord('A')-3)<0 else chr(ord(alphabet)-3) for alphabet in word ]

print("".join(l_))