import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    s=input()
    temp=[0 for _ in range(n)]
    ans=0
    for i in range(n):
        if s[i]=='L':
            temp[i]=i
        else:
            temp[i]=n-1-i
    ans=sum(temp)
    list=['' for _ in range(n)]
    for i in range(n//2):
        list[i]='R'
    for i in range(n//2+bool(n%2),n):
        list[i]='L'
    L=0;
    index=0
    # print('초기',ans)
    while L<n//2:
        R=n-1-L
        if list[L]!='' and list[L]!=s[L]:
            ans+=(n-1-L)
            ans-=(L)
            print(ans, end=' '); index+=1
        if list[R]!='' and list[R]!=s[R]:
            ans+=(R)
            ans-=(n-1-R)
            print(ans, end=' '); index+=1
        L+=1
    if ans==0: print(0, end=' ')
    else: print((str(ans)+' ')*(n-index), end=' ')
    print()