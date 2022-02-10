N,M=map(int,input().split())

arr=[]
for i in range(N):
    arr.append(list(input()))
ans=''
#M개의 글자 각각과 비교할 것이다.
for j in range(M):
    A=0
    G=0
    C=0
    T=0
    #N개의 글자를 확인할 것이다.
    for i in range(N):
        #ATGC를 각각 가정하고 최소인 것을 선택할 것이다.
        if arr[i][j]=='A': A+=1
        elif arr[i][j]=='G': G+=1
        elif arr[i][j]=='C': C+=1
        else: T+=1
    if A==max(A,G,T,C): ans+='A'
    elif C==max(A,G,T,C): ans+='C'
    elif G==max(A,G,T,C): ans+='G'
    else: ans+='T'

print(ans)
ret=0
for j in range(M):
    for i in range(N):
        if arr[i][j]!=ans[j]: ret+=1
print(ret)