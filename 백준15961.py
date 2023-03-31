import sys
input= sys.stdin.readline

N,D,k,c=map(int,input().split())
List=list(int(input()) for _ in range(N))

arr = [0 for _ in range(D+1)]

left = 0 ; right = left+k;
SUM = 0; 
coupon = 0; #1 사용할 수 있다. 0 사용할 수 없다.

#init
for i in range(left, right):
    if arr[List[i]]==0 : arr[List[i]]+=1;SUM+=1
    else: arr[List[i]]+=1


if arr[c]==0: coupon = 1
else: coupon = 0
ans = SUM+coupon




while left<N :

    if arr[List[left]]==1: SUM-=1;
    arr[List[left]]-=1

    #처리
    left+=1
    right = (left+k-1)%N
    # print(left,right)
    
    if arr[List[right]]==0: SUM+=1; 
    arr[List[right]]+=1; 

    if arr[c]==0: coupon = 1 #쿠폰 사용 가능
    else: coupon = 0;
 
    # print(SUM+coupon)
    # print(arr)
    ans=max(ans,SUM+coupon)
    
print(ans)