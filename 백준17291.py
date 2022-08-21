import sys
input=sys.stdin.readline

#DP[현재년도][분열횟수]=생성년도
DP=[[[] for _ in range(5)] for _ in range(21)]

DP[1][1].append(1)
for i in range(2,21):
    for j in range(5):
        for k in DP[i-1][j]:
            if k%2==0: #짝수년도에 탄생
                if j<4:
                    DP[i][j+1].append(k)#자기도 그대로 갈 수 있고
                if j<5:
                    DP[i][1].append(i)
            else:
                if j<3:
                    DP[i][j+1].append(k)
                if j<4:    
                    DP[i][1].append(i)
N=int(input())
# print(DP)
ans=0
for i in DP[N]:
    ans+=len(i)
print(ans)
