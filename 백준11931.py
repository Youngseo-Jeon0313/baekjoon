#자꾸 시간 초과가 뜬다ㅠㅠㅠ
import sys
input=sys.stdin.readline

t=int(input())
A=list()
for i in range(t):
    A.append(int(input()))
A.sort(reverse=True)

for i in A:
    print(i)