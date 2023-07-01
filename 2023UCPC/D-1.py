import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
List=[]
for _ in range(N):
    List.append(list(input()))

Patterns=[[[0 for _ in range(26)] for _ in range(K)]for _ in range(K)]
ans=float('inf')
ans_pattern=[]

for i in range(N):
    for j in range(M):
        Patterns[i%K][j%K][ord(List[i][j])-ord('A')]+=1
ans_pattern=[]
for a in range(K):
    temp=[]
    for b in range(K):
        lst=Patterns[a][b]
        max_value = max(lst)
        max_index = lst.index(max_value)
        temp.append(chr(max_index+ord('A')))
    ans_pattern.append(temp)
ans=0
for i in range(0,N,K):
    for j in range(0,M,K):
        for k in range(i,i+K):
            for l in range(j,j+K):
                if List[k][l]!=ans_pattern[k-i][l-j]:
                    ans+=1

print(ans)
for a in range(N//K):
    for j in range(K):
        print(''.join(ans_pattern[j]*(M//K)))

        