t=int(input())

L=list()
for i in range(t):
    L.append(list(map(int,input().split())))

S=[]
S=sorted(L,key=lambda x:[x[0],-x[1]])
S=S[::-1]
sum=0
for i in range(5, len(S)):
    if S[i][0]==S[4][0]:
        sum+=1

print(sum)

#밑에 예시 다시 보면 이해 가능!!