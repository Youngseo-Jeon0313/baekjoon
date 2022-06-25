import sys
inpyt=sys.stdin.readline
def fibo(n):
    zero=[[1,0],[0,1]]
    base=[[1,1],[1,0]]

    def matmul(a,b):
        new =[[0 for _ in range(2)] for _ in range(2)]

        for i in range(2):
            for j in range(2):
                for k in range(2):
                    new[i][j]+=a[i][k]*b[k][j]
                new[i][j]%=1000000007
        return new

    def get_nth(n):
        matrix = zero.copy()
        k=0
        tmp_matrix =base.copy()

        while 2**k <= n:
            if n & (1 << k) != 0 : #예를 들어 2^100 = 2^64 + 2^32 + 2^4 
                matrix = matmul(matrix,tmp_matrix)
            k+=1
            tmp_matrix = matmul(tmp_matrix,tmp_matrix)
        return matrix

    return get_nth(n)[1][0]

a=int(input())
print(fibo(a))


# def fibo(n):
#     sqrt_5 = 5 ** (1/2)
#     ans = 1 / sqrt_5 * ( ((1 + sqrt_5) / 2) ** n  - ((1 - sqrt_5) / 2) ** n )
#     return int(ans)

# print(fibo(int(input()))%1,000,000,007)