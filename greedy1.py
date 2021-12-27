#N으로 나누거나 K를 빼거나로 최소로!
#그냥 N으로 나눌 수 있을 '때' 바로바로 나눠준다!

n, k = map(int, input().split())

result = 0

while True:
    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) *k #k가 나누어떨어지는 수
    result += (n - target)
    n= target
    if n < k:
        break
    result += 1
    n//= k

result += (n-1)
print(result)

