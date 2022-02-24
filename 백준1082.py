'''
내 생각 중에 큰수 우선?! 이게 잘못됐음
아무리 작은 숭더라도 1111이게 99보다 크니까
긴 게 일단 우선임

'''

N=int(input())
arr=list(map(int,input().split()))
sum=int(input())
box=[0]*N
N-=1
box[N]=sum//arr[N] #
while True:
    box[N]=sum//arr[N]# 일단 최대로 넣어본다.
    sum

