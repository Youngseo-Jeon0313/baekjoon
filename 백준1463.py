'''
dp의 가장 전형적인 유형 중 점화식!
D테이블을 하나 전역에 잡고 for문을 돌면서 테이블을 채우자!!

'''
n=int(input())
d=[0]*(10**6+2)
for i in range(2,n+1):
    d[i]=d[i-1]+1
    if i%2==0: d[i]=min(d[i],d[i//2]+1)
    if i%3==0: d[i]=min(d[i],d[i//3]+1)

print(d[n])