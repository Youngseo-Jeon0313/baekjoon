import sys
input=sys.stdin.readline

N=int(input())
List=list(map(int,input().split()))
check=[0 for _ in range(10)]


flag=1
before=0
for i in range(N):
    if check[List[i]]: flag=0
    check[List[i]]=1
    if i>0:
        if before==1:
            if List[i]==3 and not check[2]: flag=0 
            if List[i]==7 and not check[4]: flag=0 
            if List[i]==9 and not check[5]: flag=0 
        elif before==2:
            if List[i]==8 and not check[5]: flag=0 
        elif before==3:
            if List[i]==1 and not check[2]: flag=0 
            if List[i]==7 and not check[5]: flag=0 
            if List[i]==9 and not check[6]: flag=0 
        elif before==4:
            if List[i]==6 and not check[5]: flag=0 
        elif before==6:
            if List[i]==4 and not check[5]: flag=0 
        elif before==7:
            if List[i]==1 and not check[4]: flag=0 
            if List[i]==3 and not check[5]: flag=0 
            if List[i]==9 and not check[8]: flag=0 
        elif before==8:
            if List[i]==2 and not check[5]: flag=0 
        elif before==9:
            if List[i]==1 and not check[5]: flag=0 
            if List[i]==3 and not check[6]: flag=0 
            if List[i]==7 and not check[8]: flag=0 
            
    before=List[i]

if flag: print("YES");
else: print("NO")