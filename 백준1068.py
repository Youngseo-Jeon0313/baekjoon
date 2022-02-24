'''
쉽게 생각해보자.
그렇게 받은 부모노드들을 차곡차곡 저장해서

'''

N=int(input())
arr=list(map(int,input().split()))
D=dict()
for i in range(len(arr)):
    D[arr[i]]=i
sorted(D.items(), key=lambda x: x[1])

money=int(input())
ans=[]
for i in range(money//D.values()[0]):
    ans.append(D.values()[0])
money%=D.values()[0] #일단 제일 작은 걸로 길게 한 후 남은 거스름돈
sum=0
for i in ans: 
    if sum<money:
        