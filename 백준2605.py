N=int(input())
List=list(map(int,input().split()))

ans=[]

#그만큼 앞으로 간다.
for i in range(N):
    ans.insert(i-List[i],i+1)
    # print(ans)

print(*ans)