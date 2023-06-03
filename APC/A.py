import sys
input=sys.stdin.readline

s=int(input())
ans=0
for j in range(1,1+s):
    # print(j)
    if '50' in str(j): 
        # print(j)
        ans+=1
if '50' in str(s): 
    print(s+ans-1)
else:
    print(s+ans)