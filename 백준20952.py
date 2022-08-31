import sys
input = sys.stdin.readline
MOD=1000000007
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
arr=[0,0,0,0,0,0,0] #0,1,2,3,4,5,6
ans=0

for i in A:
    if arr[i%7]==0: ans+=1; arr[i%7]=1


finalB=0
for i in range(M):
    check=(7-(B[i]+finalB)%7)%7
    if arr[check]==1: #아직 안 지워진 값이라면
        if ans==1: continue; #다 지워지려고 하면 원상복귀
        else: #연산 적용
            arr[check]=0; ans-=1; 
    finalB+=B[i]#지워져야 하는 순간 ans-=1하고

ansarr=[]
for i in range(N):
    if arr[A[i]%7]==1: ansarr.append((A[i]+finalB)%MOD)
print(len(ansarr))
print(*ansarr)


'''
7 5
1 2 3 4 5 6 7
1000000000 1000000000 1000000000 1000000000 1000000000

답
2
999999978 999999979
'''