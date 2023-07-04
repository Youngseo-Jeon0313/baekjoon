N=int(input())
ans=0
for _ in range(N):
    dict={}
    temp=0
    a,b,c,d=map(int,input().split())
    List=[a,b,c,d]
    List=sorted(List)
    if List[0]==List[1] and List[1]==List[2] and List[2]==List[3]:
        temp+=50000+List[1]*5000


    elif List[0]!=List[1] and List[1]==List[2] and List[2]==List[3]:
        temp+=10000+List[1]*1000
    elif List[0]==List[1] and List[1]==List[2] and List[2]!=List[3]:
        temp+=10000+List[1]*1000


    elif List[0]==List[1] and List[1]!=List[2] and List[2]==List[3]:
        temp+=2000+List[0]*500+List[2]*500


    elif List[0]!=List[1] and List[1]!=List[2] and List[2]==List[3]:
        temp+=1000+List[2]*100
    elif List[0]==List[1] and List[1]!=List[2] and List[2]!=List[3]:
        temp+=1000+List[0]*100
    elif List[0]!=List[1] and List[1]==List[2] and List[2]!=List[3]:
        temp+=1000+List[1]*100
    
    else: temp+=List[-1]*100
    ans=max(ans,temp)
print(ans)