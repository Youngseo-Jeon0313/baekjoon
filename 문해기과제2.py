def count_coprime(A, B, N):
    ans = B - A + 1  
    for prime in range(2, N + 1):
        if N % prime == 0:
            # prime이 N의 약수인 경우, prime의 배수를 제외
            for i in range((A + prime - 1) // prime, B // prime + 1):
                num = i * prime
                if A <= num <= B:
                    ans -= 1
    return ans

A, B, N = map(int, input().split())

# N을 소인수분해하고, 각 소인수에 해당하는 배수를 제외한 수의 개수를 구하기
ans = count_coprime(A, B, N)

print(ans)
