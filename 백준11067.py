import sys
input=sys.stdin.readline


from collections import deque
T=int(input())
for _ in range(T):
    n=int(input())
    temp=[]
    for _ in range(n):
        x,y=map(int,input().split())
        temp.append([x,y])
    temp.sort()

    L=[]
    for i in temp:
        if L and L[-1][0][0]==i[0]: L[-1].append(i)
        else:L.append([i])
    y=0
    # print(L)
    ans=[]
    for i in L:
        if i[0][1]==y: ans.extend(i); y=i[-1][1]
        else: y=i[0][1];ans.extend(i[::-1]); 
    # print(ans)
    Ans=list(map(int,input().split()))

    for i in range(1,1+Ans[0]):
        print(*ans[Ans[i]-1])
