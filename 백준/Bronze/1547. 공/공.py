ball=1
N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    if a==ball:
        ball=b
    elif b==ball:
        ball=a
print(ball)