'''
N명의 병사가 무작위로 나열되어 있다. 각 병사는 특정한 값의 전투력을 보유하고 있다.
병사를 배치할 떄 전투력이 높은 병사가 맨 앞으로 오도록 하고 싶다.
또한 배치 과정에서 특정한 위치에 있는 병사를 열외시키는 방법을 사용하려고 한다.
'''

#가장 긴 증가하는 부분수열(LIS, Longest Increasing Subsequence)
#모든 0<=j<i 에 대하여 D[i] = max(D[i], D[j]+1) if array[j] < array[i]
#LIS = 각 각의 원소가 '마지막 원소'라고 했을 때 
n=int(input())
array = list(map(int,input.split()))
array.reverse()

dp=[1]*n

for i in range(1,n):
    for j in range(0,i):
        if array[j]<array[i]:
            dp[i] = max(dp[i],dp[j+1])

print(n-max(dp))
