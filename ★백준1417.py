from heapq import *
n=int(input())
val=int(input()) #기호 1번 다솜이의 득표수
ans=0
if n==1:
    print(0)
    exit()

hq=[]
for i in range(1,n):
    heappush(hq,-int(input())) #음수로 해서 heap에 넣어준다

#다솜이가 국회의원 될 때까지 while문 돌림
while val <= -hq[0]: #다솜이가 다른 애들보다 득표율 작아?
    x = heappop(hq) 
    x+=1; val+=1; ans+=1 #매수하고 다솜이 득표수하나 올리고/상대편 득표수 하나 내리고 다시 turn~ 
    heappush(hq,x)

print(ans)