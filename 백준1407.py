'''
구간에 대해 모든 수를 체크하면 시간초과 됨 ㅠㅠ

a, b = map(int, input().split())
Ans=0
for x in range(a,b+1):
    i=1
    while i<=x:
        if x%i==0:
            ans=i
        i*=2
    Ans+=ans
print(Ans)

'''
def divid2(num):
    i=1
    ans=0
    while i<=num:
        a=(num//i)
        b=(num//(2*i))
        ans+=i*(a-b)
        i*=2
    return ans
a,b=map(int,input().split())
print(divid2(b)-divid2(a-1))


'''
think
어차피 2로 나눈게 **그 때 까지 나오는 2의 배수들
어차피 4로 나눈게 **그 때까지 나오는 4의 배수들
이런 식으로
재귀



'''