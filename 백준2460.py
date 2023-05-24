ans=0
people=0
for i in range(10):
    a,b=map(int,input().split())
    people=people-a+b
    ans=max(ans,people)

print(ans)