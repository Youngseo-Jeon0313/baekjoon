import sys
input=sys.stdin.readline

N=int(input())
#DP [몇자리 수인지][비트마스크]=해당숫자들 나열
#DP는 0부터 9중 뭘 썼는지 파악하기 위해서 사용한다.
#0000000010 은 1만 쓴 거임 ex. 1, 11, 111 등 
DP=[[[] for _ in range(1024)] for _ in range(N+1)]
for i in range(1,10):
    DP[1][1<<i].append(i)

for i in range(2,N+1): #N=1일 때 N=2일 때 .. 쭉쭉 해결해보자
    for j in range(1024): #비트마스킹
        for k in DP[i-1][j]: #DP안에 들어있는 애들과
            #0을 붙여본다.
            for l in range(1,10):
                if j&(1<<(9-l))==0:
                    DP[i][j|(1<<l)].append(k*10+l)
print(DP)
ans=[]
for i in range(1024):
    ans.extend(DP[N][i])
print(ans)
print(len(ans))

            

