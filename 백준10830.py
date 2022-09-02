import sys
input=sys.stdin.readline

N,B=map(int,input().split())
MOD=1000
A=[]
for _ in range(N):A.append(list(map(int,input().split())))

#행렬 곱 계산
def matrix_pow(a,b):
    List=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                List[i][j]+=a[i][k]*b[k][j]
            List[i][j]%=MOD
    return List


def fpow(c,n): #행렬, 몇제곱
    if n==1: 
        for i in range(N):
            for j in range(N):
                c[i][j]%=MOD
        return c
    else: 
        x=fpow(c,n//2)
        if n%2:return matrix_pow(matrix_pow(x,x),c)
        else: return matrix_pow(x,x)


ANS=fpow(A,B)
# print(ANS)
for i in ANS:
    for j in i:
        print(j%MOD, end=' ')
    print()