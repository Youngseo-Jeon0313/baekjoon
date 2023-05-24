N=int(input())
List=list(map(int,input().split()))
ans=sum(List)+8*(N-1)
print(ans//24, ans%24)