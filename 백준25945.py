import sys
input=sys.stdin.readline

N = int(input())
List = list(map(int,input().split()))

# 일단 정렬
List = sorted(List)
#한 칸당 어느정도 있어야 하는 갯수
share = sum(List) // N
remainder = sum(List) % N

target = [share] * (N-remainder) + [share+1] * remainder

answer = 0
for i in range(N):
    answer+=abs(List[i]-target[i])


print(answer//2)