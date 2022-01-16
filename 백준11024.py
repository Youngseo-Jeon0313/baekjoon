t=int(input())

for i in range(t):
    A=list(map(int, input().split()))
    sum=0
    for i in A:
        sum+=i
    print(sum)