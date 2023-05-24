n=int(input())
List=list(map(int,input().split()))
ans=[0 for _ in range(n)]
for i in range(n):
    if List[i]==0:
        continue
    else:
        ans[i]=ans[i-1]+1

# print(ans)
print(sum(ans))