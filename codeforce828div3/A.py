T=int(input())
for _ in range(T):
    n=int(input())
    L=list(map(int,input().split()))
    S=str(input())
    flag=True
    Dict={}
    for i in range(n):
        if L[i] in Dict.keys():
            if S[i]!=Dict[L[i]]:
                flag=False
        else:
            Dict[L[i]]=S[i]
    if flag:print('YES') 
    else:print("NO")