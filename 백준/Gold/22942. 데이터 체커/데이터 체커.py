import sys
input=sys.stdin.readline

N=int(input())
List=[]
for i in range(N):
    x,y=map(int,input().split())
    List.append((x-y,i))
    List.append((x+y,i))
List=sorted(List)


stack=[]
for j in List:
    if stack: 
        if stack[-1]==j[1]:
            stack.pop()
        else:
            stack.append(j[1])
    else: stack.append(j[1])

if stack : print("NO")
else: print("YES")