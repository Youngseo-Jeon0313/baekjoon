S=input()
T=input()
i=0; j=0;
ans=0

flag=True
for a in S:
    if a not in T:
        flag=False
if flag==True:
    while i<len(S):
        if j%len(T)==0:ans+=1 #여기 ans가 처음에 들어가는 것이 옳다!
        if S[i]==T[j%len(T)]:
            i+=1; j+=1
        else:
            j+=1
        

    print(ans)
else:
    print(-1)

#시간복잡도 ㅒO(100만+100만)