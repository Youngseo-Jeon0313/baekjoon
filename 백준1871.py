N=int(input())
for _ in range(N):
    a,b=input().split('-')
    temp=0
    for i in range(len(a)):
        temp+=(ord(a[i])-ord('A'))*(26**(len(a)-i-1))
    # print(temp)
    ans=abs(temp-int(b))
    # print(ans)
    if ans<=100: print('nice')
    else: print('not nice')