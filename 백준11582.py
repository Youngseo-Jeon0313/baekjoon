import sys
input=sys.stdin.readline

N=int(input())
num_list=list(map(int,input().split()))

K=int(input()) #현재 정렬을 진행중인 회원의 수

new_list=[0 for _ in range(N)]

for i in range(K):
    templist=num_list[i*N//K:i*N//K+N//K]
    tempList=templist.copy()
    tempList.sort()
    for j in range(N//K):
        new_list[N//K*i+j]=tempList[j]


print(*new_list)