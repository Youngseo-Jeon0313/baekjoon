import sys
input=sys.stdin.readline
#분할정복 +  나머지 분배 법칙?????? 아오;;;
# (AxB)%C = (A%C) *(B%C) % C
a,b,c=map(int,input().split())
def divide(a,n):
    #가장 밑 분할 노드 도착
    if n==1: 
        return a%c
    else:
        #분할해서 간 결과값1
        #분할해서 간 결과값2
        temp=divide(a,n//2)
        #그걸 이용해서 합쳐서 정복
        if n%2==0: #짝수라면 10^10 = (10^5)^2 형태
            return (temp*temp)%c
        else: #홀수라면 (10^5)^2*10 형태
            return (temp*temp*a)%c
print(divide(a,b))