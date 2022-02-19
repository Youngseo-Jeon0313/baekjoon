#two pointer
import sys
input=sys.stdin.readline
n, s=map(int,input().split())
arr = [*map(int,input().strip().split())] #공백 제거 strip
l,r=0,0 #left, right pointer
val =0
ans = float('inf')
while True:
    #s보다 크면 혹시나 하면서 left를 오른쪽으로 한칸씩 옮김
    if val >= s:
        ans=min(ans, r-l)#갱신(할수 있다면 ㅇ)
        val-=arr[l]
        l+=1
    elif r==n: break #끝까지 다 가봄
    #s보다 작으면 늘리기 위해서
    else:
        val+=arr[r]
        r+=1
if ans==float('inf'):print(0)
else: print(ans)
