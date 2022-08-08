import sys
input=sys.stdin.readline

N,X=map(int,input().split())
#배낭문제..
DP=[0 for _ in range(X+1)] 

DP[0]=1

for _ in range(N):
    x,y=map(int,input().split())
    for i in range(X,-1,-1):
        if DP[i] :
            for k in range(y,0,-1):    
                if i+k*x<=X :DP[i+k*x]+=DP[i]


print(DP)

print(DP[X])