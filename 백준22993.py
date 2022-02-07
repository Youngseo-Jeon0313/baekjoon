N=int(input())
s=list(map(int, input().split()))
J=s[0]
s.pop(0)
s.sort()
flag=True
for i in range(N-1):
    if J>s[i]:
        J+=s[i]
    else:
        flag=False
        break
if flag==True: print('Yes')
else: print('No')