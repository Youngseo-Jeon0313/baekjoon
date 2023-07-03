N,K=map(int,input().split())
List=list(map(int,input().split()))
Max=0
for i in List:
    Max+=i//2+bool(i%2)
if Max>=N: print('YES')
else: print("NO")