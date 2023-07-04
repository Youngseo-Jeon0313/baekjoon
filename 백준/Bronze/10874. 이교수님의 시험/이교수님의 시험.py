N=int(input())
arr=[]
for k in range(N):
    List=list(map(int,input().split()))
    ans=0
    for i in range(1,11):
        if List[i-1]==(i-1)%5+1:
            ans+=1
    if ans==10: arr.append(k+1)
for i in arr:
    print(i)