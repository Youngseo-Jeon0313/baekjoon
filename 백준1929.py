M,N=map(int,input().split())
#제곱근까지만 해서 소수 판별하는 함수
#별로 ㄴ안중요..
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

for i in range(M,N+1):
    if isPrime(i): print(i)
