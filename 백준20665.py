import sys
inpyt=sys.stdin.readline
N,T,P=map(int,input().split()) #자리 개수,독서실 예약자 수, 민규가 좋아하는 좌석 번호
seatList=[[0 for _ in range(12*60)] for _ in range(N)] 
memList=[]

for _ in range(T):
    IN,OUT=input().split()
    IN=int(IN[0:2])*60+int(IN[2:4])-540
    OUT=int(OUT[0:2])*60+int(OUT[2:4])-540
    memList.append([IN,OUT])
memList.sort(key = lambda x: (x[0], x[1]))

for i in memList:
    flag=True
    for j in range(N):
        for k in range(i[0],i[1]):
            if seatList[j][k]!=0: flag=False; break
        if flag==False: break
    
    if flag==True:
        for j in range(i[0],i[1]): seatList[0][j]=1
    else:
        #for문으로 자리 판단해서 채운다
        max=0
        for k in range(N-1,-1,-1): #빈 곳이야
            localmin=float('inf')
            for j in range(N): #채워진 곳이야
                # print(seatList[k][i[0]:i[1]+1])
                # print(seatList[j][i[0]:i[1]+1])
                if (1 not in seatList[k][i[0]:i[1]]) and (1 in seatList[j][i[0]:i[1]]):
                    if abs(k-j)<=localmin:localmin=abs(k-j); localnum=k
            if localmin!=float('inf') and max<=localmin: max=localmin; maxnum=localnum       
        for j in range(i[0],i[1]):
            seatList[maxnum][j]=1
ans=0
for i in range(720):
    if seatList[P-1][i]==0:ans+=1

print(ans)