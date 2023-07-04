N,M=map(int,input().split())
List=list(map(int,input().split()))
ANS=[]
for i in range(1,N+1):
    for j in (List):
        if i%j==0: ANS.append(i)
ANS=list(set(ANS))
print(sum(ANS))