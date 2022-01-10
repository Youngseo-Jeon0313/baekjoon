input = __import__('sys').stdin.readline
n = int(input())
sum=0
for i in range(n):
    sum+=int(input())

if sum <= n//2:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")