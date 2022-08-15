import heapq
import sys
input=sys.stdin.readline

K,N=map(int,input().split())
NumList=list(map(int,input().split()))
hq=[]
heapq.heapify(hq)
for i in NumList:heapq.heappush(hq,i)

turn=0
while True:
    a=heapq.heappop(hq); turn+=1;
    for i in NumList:
        heapq.heappush(hq,i*a)
        if a%i==0: break; #뒤의 배수로 이어지는 애들은 그냥 걔들이 처리하도록 하기
    if turn==N: print(a); exit()

