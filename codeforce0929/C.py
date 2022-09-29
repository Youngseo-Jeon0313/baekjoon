T=int(input())
for _ in range(T):
    n=int(input())
    dict={}
    first=list(input().split())
    second=list(input().split())
    third=list(input().split())
    for i in first:
        dict[i]=1
    for j in second:
        if j in dict.keys():
            dict[j]+=1
        else:
            dict[j]=1
    for k in third:
        if k in dict.keys():
            dict[k]+=1
        else:
            dict[k]=1
    firstscore=0; secondscore=0; thirdscore=0;
    for i in first:
        if dict[i]==1: firstscore+=3
        elif dict[i]==2: firstscore+=1
    for j in second:
        if dict[j]==1: secondscore+=3
        elif dict[j]==2: secondscore+=1
    for k in third:
        if dict[k]==1: thirdscore+=3
        elif dict[k]==2: thirdscore+=1
    print(firstscore, secondscore, thirdscore)