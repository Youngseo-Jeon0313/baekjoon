N=int(input())
ans=0
Lines=[0]
for _ in range(N):
    a,b=map(int,input().split())
    while Lines and Lines[-1]>=b:
        if Lines[-1]>b:     
            ans+=1
            Lines.pop()
        else:
            Lines.pop()
    Lines.append(b)
    # print('답',ans)
a,b=1000001,0;
while Lines and Lines[-1]>=b:
    if Lines[-1]>b:     
        ans+=1
        Lines.pop()
    else:
        Lines.pop()
Lines.append(b)
print(ans)