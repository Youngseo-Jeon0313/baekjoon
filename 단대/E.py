N,l,Q=map(int,input().split())
Request=[]
Pizza=[0 for _ in range(N)]
for _ in range(Q): Request.append(list(map(int,input().split())))

print(Request)
print(Request[0])
for i in range(Q):
    if Request[i][0]==1:
        Pizza[Request[i][1]-1]=Request[i][2]
    if Request[i][0]==2:
        Pizza[Request[i][1]-1]=0
    print(Pizza)
