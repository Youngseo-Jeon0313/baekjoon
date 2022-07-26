
import sys
input=sys.stdin.readline
from collections import deque 

H=int(input())
List=[0,0]
leaf=[]

List.extend(list(map(int,input().split())))
for i in range(2**H,2**(H+1)):
    j=i
    SUM=0
    while j>1:
        SUM+=List[j]
        j//=2
    leaf.append(SUM)
leaf=deque(leaf)


ans=sum(List) #여기에 답을 더할 것임
Max=max(leaf) #값을 맞추기 위해 max값을 구함


for i in range(len(leaf)):
    a=leaf.popleft()
    leaf.append(Max-a)




while len(leaf)>1:
    a=leaf.popleft()  
    b=leaf.popleft()
    c=min(a,b)
    ans+=(a-c+b-c)
    leaf.append(c)

print(ans)