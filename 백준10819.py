N=int(input())
arr=list(map(int,input().split()))

#재귀함수로 구현한다.
#모든 조합을 구한다 combination 사용

from itertools import permutations
A=permutations(arr,N)
max=0
for i in A:
    sum=0
    for j in range(N-1):
        sum+=abs(i[j]-i[j+1])
    if sum>max:
        max=sum
print(max)
