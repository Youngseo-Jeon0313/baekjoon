N,M=map(int,input().split())
List=list(map(int,input().split()))
Gap=[0 for _ in range(N)]
for i in range(1,N):
    Gap[i-1]=List[i]-List[i-1]

for _ in range(M):
    From,To=map(int,input().split())
    Before=List[From-1]
    Gap[From-2]+=(To-Before)
    Gap[From-1]-=(To-Before)
    List[From-1]=To
    #print(Gap)
    #print(List)
    plus=Gap[0]
    mod=List[1]/List[0]
    flagplus=True; flagmod=True;
    if plus <=0: flagplus=False;
    if mod <=0: flagmod=False;
    for i in range(1,N-1):
        if List[i+1]/List[i] != mod: flagmod=False;
        if Gap[i] != plus : flagplus=False;
    if flagplus==True : print('+'); 
    elif flagmod==True: print('*')
    else: print('?')

    