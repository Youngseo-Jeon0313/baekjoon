n=39
ans=0
ddlist=[]
for i in range(len(str(n))):
    ddlist.append(str(n)[i])

for i in range(len(str(n))):
    ans+=int(ddlist[i])
ans+=n
