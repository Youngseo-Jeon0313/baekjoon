import sys
input=sys.stdin.readline
'''
처음 생각은 cb로 가능한 경우를 하나씩 판단해서 집어넣는 것이었는데,
그렇게 하지 않고 배낭 문제로 구현할 수 있다.

'''



N,M=map(int,input().split())
R=[]
B=[]
D=[]
DP=[[-1 for _ in range(101)] for _ in range(101)]
DP[0][0]=0
for x in range(M):
    r,b,d=map(int,input().split())
    R.append(r); B.append(b); D.append(d)

for i in range(M):
    now_r=R[i]; now_b=B[i]
    for a in range(50,-1,-1):
        for b in range(50,-1,-1):
            if a-now_r >=0 and b-now_b>=0 and DP[a-now_r][b-now_b]!=-1:
                DP[a][b]=max(DP[a][b],DP[a-now_r][b-now_b]+D[i])
    # for i in range(10):
    #     for j in range(10):
    #         print(DP[i][j],end='')
    #     print()
ans1=[]
ans2=[]
for i in range(N):
    a,b=map(int,input().split()) #a==0 b==0인 경우도 생각해줘야 함....
    if DP[a][b]==-1 or DP[a][b]==0: ans1.append([i+1,0])
    else:ans2.append([i+1,DP[a][b]])
# print(ans)
ans2=sorted(ans2,key=lambda x:x[1])

for k in ans1:
    print(k[0],k[1])
for l in ans2:
    print(l[0],l[1])