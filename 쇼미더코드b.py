N,Q=map(int,input().split())
arr=list(input().split()) #각각의 대문에 쓰여있는 수 (우리가 합칠 수)
Tree={}
for _ in range(N-1):
    ai,bi=map(int,input().split())
    if ai in Tree: Tree[ai].append(bi);
    else:Tree[ai]=[bi];
    if bi in Tree: Tree[bi].append(ai);
    else: Tree[bi]=[ai]
AAAAANNNNSSSS=[]
#여기서부턴 방문체크 이용!!
from collections import deque
q=deque()
for _ in range(Q):
    val=2
    check=[0]*(N) #얘는 0부터 index시작하는 거 주의하자!!
    xi,yi=map(int,input().split())
    #자 게임을 시작하지
    q=[yi]
    check[yi-1]=1
    while q:
        x=q.pop()
        if x in Tree:
            for i in Tree[x]:
                if not check[i-1]: 
                    q.append(i); check[i-1]=val
        val+=1

    num=check[xi-1]
    parent=xi
    Ans=arr[xi-1]
    while num>0:
        num-=1
        for i in Tree[parent]:
            if check[i-1]==num: Ans+=arr[i-1]; parent=i
    AAAAANNNNSSSS.append(int(Ans)%1000000007)
for i in AAAAANNNNSSSS:
    print(i)