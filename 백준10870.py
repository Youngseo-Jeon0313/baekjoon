import sys
input=sys.stdin.readline

fibo=[0, 1, 1]

for i in range(20):
    fibo.append(fibo[-1]+fibo[-2])
n=int(input())
print(fibo[n])