N=int(input())

A=list(map(int, input().split()))


A=list(set(A))
A.sort()

for i in A:
    print(i, end=' ')

#자꾸 튜플이랑 set을 혼동하는데 튜플은 '값이 변하지 않는다'가 가장 큰 특징임!