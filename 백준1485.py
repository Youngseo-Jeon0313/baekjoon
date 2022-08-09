T=int(input())
for _ in range(T):
    List=[]
    for i in range(4):
        x,y=map(int,input().split())
        List.append([x,y])
    List=sorted(List,key=lambda x: [x[0],x[1]])
    print(List)
    if List[0][0]==List[1][0] and List[2][0]==List[3][0] and List[0][1]==List[2][1] and List[1][1]==List[3][1] and List[1][1]-List[0][1]==List[2][0]-List[0][0]:
        print(1)
    else: print(0)