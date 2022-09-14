'''
기존의 LIS는 for문 두 개로 해결해서 O(N^2)으로 해결할 수 있었으나
이 문제는 O(logN)으로 해결하는 방법을 요구
'''
'''
핵심은  '어차피!'

어차피 그걸로 대체해도 상관없어!
'''
import sys
input=sys.stdin.readline

N=int(input())
L=list(map(int,input().split()))
List=[1]
for i in L:
    if List[-1]<i:List.append(i)
    else:
        #포인터 방식으로 적절한 위치 찾아가자!
        left=0; right=len(List);
        #이진탐색
        while left<right:
            mid=(left+right)//2
            if List[mid]<i:left=mid+1
            else: right=mid
        List[right]=i


print(len(List)-1)