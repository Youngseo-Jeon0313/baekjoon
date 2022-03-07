'''
내 생각 중에 큰수 우선?! 이게 잘못됐음
아무리 작은 숭더라도 1111이게 99보다 크니까
긴 게 일단 우선임
DP


알고리즘이 미쳤다.....
dp + 수학적 지식 가지고 푸는 문제인 듯

'''
N=int(input())
arr=list(map(int,input().split()))
sum=int(input())

D={}
for i in range(len(arr)):
    D[i]=arr[i]
#(숫자,가격)으로 튜플 형식으로 리스트가 나오게 된다
D=sorted(D.items(), key=lambda x:x[1])

dp=[-1000]*(sum+1)
for i in range(len(D)-1,-1,-1):
    for k in range(D[i][1],sum+1):
        #처음엔 모두 -1000으로 되어 있다는 걸 명심하자!
        dp[k]=max(dp[k-D[i][1]]*10+D[i][0],dp[k],D[i][0])
print(dp[-1])












'''
INF = 5001
n = int(input())
room = list(map(int, input().split()))
m = int(input())
dp = [-INF for _ in range(m+1)]
for i in range(n-1, -1, -1):
    x = room[i]
    for j in range(x, m+1):
        dp[j] = max(dp[j-x]*10+i, i, dp[j])

print(dp[m])
'''