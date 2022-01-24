players=int(input())
CHECK=[[],[],[]]
L=[]
for k in range(players):
    a,b,c=input().split()
    A,B,C=a,b,c
    if len(L)==0:
                L.append([a,b,c])
                continue
    for i in range(k):
            if L[i][0]==a:
                L[i][0]=0
                CHECK[0].append(a)
                a=0
            elif a in CHECK[0]:
                a=0
            if L[i][1]==b:
                L[i][1]=0
                CHECK[1].append(b)
                b=0
            elif b in CHECK[1]:
                b=0
            if L[i][2]==c:
                L[i][2]=0
                CHECK[2].append(c)
                c=0    
            elif c in CHECK[2] :
                c=0
    L.append([a,b,c])

for i in range(players):
    sum=0
    for j in range(3):
        sum+=int(L[i][j])
    print(sum)
