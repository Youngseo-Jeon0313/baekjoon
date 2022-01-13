n=int(input())
ans = 0
while n >= 3:
    if n % 5 == 0:
        #5가 더 좋은 거니까 5로 팍 나눠질 때까지 3으로 나누기
        ans += n//5
        n = 0
        break
    else:
        n -= 3
        ans += 1
if n > 0:
    print(-1)
else:
    print(ans)