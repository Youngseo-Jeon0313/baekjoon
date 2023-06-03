a,b,c=map(int,input().split())
List=[a,b,c]
List=sorted(List)
res=input()
for i in range(3):
    if res[i]=='A': print(List[0],end=' ')
    elif res[i]=='B': print(List[1],end=' ')
    else: print(List[2],end=' ')