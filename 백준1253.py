import sys
input=sys.stdin.readline

#투포인터 + 이분탐색
#수의 위치가 다르면 값이 같아도 다른 수이다. 이게 핵심!
N=int(input())
NumList=list(map(int,input().split()))
NumList.sort()
ans=0

for i in range(N): 
    target=NumList[i] #target 이라는 숫자가 GOOD인지 판단하자.
    temp=NumList[:i]+NumList[i+1:]
    lo,hi=0, len(temp)-1
    while lo<hi:
        sum=temp[lo]+temp[hi]
        if sum==target:
            ans+=1; break;
        elif sum<target: lo+=1
        else: hi-=1
print(ans)
