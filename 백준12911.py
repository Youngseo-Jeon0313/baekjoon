import sys
input=sys.stdin.readline
MOD=1000000007
N,M=map(int,input().split())

'''
문제에서 주어지는 메모리 제한이 512MB라고 할 때 대략 int 1.2억개 정도의 배열을 잡을 수 있음
'''

SUM1=M
SUM2=0
for j in range(1,M+1):
    if j==1: SUM2+=1
    else:
        SUM2+=M-M//j+1

print(SUM1,SUM2)
diff=SUM2-SUM1
# if M==2: print(SUM2)
# elif M==2: print(SUM1)
# else:
#     
print((SUM1+diff*(N*(N-1)//2))%1000000007)

'''

3 2 4

'''
