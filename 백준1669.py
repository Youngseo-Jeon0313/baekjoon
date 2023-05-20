'''
시간초과 안난다고 해도 -> 메모리초과
수학

규칙 생각 1 2 3 2 1 -> 제곱의 ..뉘앙스
'''
import sys
iput=sys.stdin.readline

X,Y=map(int,input().split())

DP=[0]
check=0
for i in range(40000):
    if i%2: DP+=[i-1]*(i//2)
    else: 
        DP+=[i-1]*(i//2)
    
print(DP[Y-X])