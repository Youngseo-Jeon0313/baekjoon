import sys
input=sys.stdin.readline
n=int(input())
L=list(map(int,input().split()))
L.sort(key=lambda x:abs(x))
ans=['0','0']
min_sum=float('inf')
for start in range(n-1):
    end=start+1
    while end<n:
        if abs(L[end]+L[start])<min_sum:ans[0]=L[start];ans[1]=L[end]; min_sum=abs(L[end]+L[start])
        if abs(L[end]+L[start]) >= min_sum : break;
        end+=1

if ans[0]<ans[1]: print(ans[0],ans[1])
else: print(ans[1],ans[0])

