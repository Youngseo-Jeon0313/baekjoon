t=int(input())

name=input()
ans=0
for i in range(t):
    ans+=ord(name[i])-64

print(ans)