s=input()

S='CAMBRIDGE'
s=list(s)
j=0
i=0
while True:
    if j==len(s):
        break
    for k in S:
        flag=False
        for i in range(len(s)-j):
            if s[i]==k:
                s.pop(i)
                j+=1
                flag=True
                break
        if flag==False:
            
        
print(''.join(s))