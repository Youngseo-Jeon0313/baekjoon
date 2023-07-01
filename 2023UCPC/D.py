import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
List=[]
for _ in range(N):
    List.append(list(input()))

#가능한 패턴을 모두 집어넣는다.
patterns=[]
a=0; b=0
for i in range(a,a+N//K):
    for j in range(b,M,K):
        temp=[]
        for k in range(i,i+K):
                temp.append(List[k][j:j+K])
        patterns.append(temp)
        b=(b+K)%M
    a=(a+K)%N; 
ans=float('inf')
ans_pattern=[]
for pattern in patterns:
    error=0
    for i in range(a,N,K):
        for j in range(b,M,K):
            for k in range(i,i+K):
                for l in range(j,j+K):
                    if List[k][l]!=pattern[k-i][l-j]:
                        error+=1
            b=(b+K)%M
        a=(a+K)%N; 
    if error<ans: ans=error; ans_pattern = pattern     

print(ans)
print(ans_pattern)
for a in range(N//K):
    for j in range(K):
        print(''.join(ans_pattern[j]*(M//K)))
    