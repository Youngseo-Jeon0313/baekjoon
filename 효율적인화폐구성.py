#N가지 종류가 존재하고 최소한의 개수로 M을 만드는 방법

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input())) #enter치고 넘어가야 함

d=[10001] * (m+1) #초기화는 10001로

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1): #array속 숫자에서부터 내가 적은 숫자까지 
        #(i-k)원을 만드는 방법이 존재하는 경우
        if d[j-array[i]] != 10001: #d배열을 하나씩 훑어봤을 때 10001이 아니면 (예를 들면 우리가 지정한 10은 10-10 = 0 되니까 0번째 d배열은 0임)
            d[j] = min(d[j], d[j-array[i]]+1) #그 중 최소가 되도록 그냥 자기자신이 되던가 아니면 그 전꺼 중에 +1

#계산된 결과 출력
if d[m] == 10001:
    print(-1)
else :
    print(d[m])

'''
d배열은-> 0 10001 
3 100
5
10
26
-------
10
'''