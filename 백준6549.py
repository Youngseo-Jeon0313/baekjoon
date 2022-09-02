import sys
input=sys.stdin.readline

while True:
    L=list(map(int,input().split()))
    if len(L)==1 and L[0]==0: break
    L+=[0]
    ans=0
    stack=[]
    for i in range(1,L[0]+2):
        ans=max(ans,L[i])
        if len(stack)==0:stack.append([i,L[i]]); continue;#맨 처음에 입력받았을 경우
        flag=False; index=i #나랑 같은 게 나올 경우 그 index로 바꿔주기 위함
        while len(stack) and stack[-1][1]>L[i]: #나보다 큰 게 나올 때마다 뺀다.
            #print('전',stack)
            index,height=stack.pop()
            ans=max(ans,height*(i-index))
            #print('후',stack)
            #print(ans)
        stack.append([index,L[i]]) #내가 제일 작으니까
    print(ans)