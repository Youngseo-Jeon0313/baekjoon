from re import L
import sys
input=sys.stdin.readline

N=int(input())

num=[0]*10001

for _ in range(N):
    temp=int(input())
    num[temp]+=1
for i in range(10001):
    if num[i]!=0:
        for j in range(num[i]):
            print(i)
'''
그냥 sort로 하면 문제가 생긴다.
왜냐?? 똑같은 수가 두 개가 나올 수 있을 때 그게 좀 문제가 되므로
10000보다 어차피 작거나 같은 수가 나오니까 그 수를 발견했냐?? 그러면 출력~ 
그리고 그 수가 몇 개 있는데? 그 숫자만큼 출력할게
이런 식으로 가는 게 낫다
'''