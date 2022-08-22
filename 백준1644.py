import sys
input=sys.stdin.readline

n=4000000
a = [True]*(n+1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

N=int(input())
#투포인터,누적합의 핵심은 연속된 어떤 구간 안에서의 처리이다.

left, right = 0, 0
cnt = 0
while right<=len(primes) and left<=right:
    sum_nums = primes[left:right]
    total = sum(sum_nums)
    if total == N:
        cnt += 1
        right += 1
    elif total < N:
        right += 1
    else:
        left += 1

print(cnt)