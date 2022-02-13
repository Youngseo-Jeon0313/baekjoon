'''
fibo(n)을 호출할 때 fibo(n-1)의 0과 1의 호출 개수 + fibo(n-2)의 0과 1의 호출개수랑 같음

'''


def fibo(n):
    if n>=len(zero):
        for i in range(len(zero),n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])   

zero=[1,0,1]; one=[0,1,1]
t=int(input())
for i in range(t):
    n=int(input())
    fibo(n)
    print(zero[n],one[n])
