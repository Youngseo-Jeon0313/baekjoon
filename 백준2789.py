s=input()

S='CAMBRIDGE'
s=list(s)


for i in range(len(s)):
    while True:
        for j in S:
            if j==s[i]:
                s.pop(i)
                break
print(''.join(s))