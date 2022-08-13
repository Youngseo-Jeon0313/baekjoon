import sys
input=sys.stdin.readline

def div_conquer(start, end):
    global ans
    #가장 밑 분할 노드 도착했을 때 return
    if start==end :
        return List[]
    #그게 아니면
    #분할해서 간 결과값 1
    a=div_conquer( )
    #분할해서 간 결과값 2
    b=div_conquer( )
    #그걸 이용해 합치든가 뭘 해서 암튼 정복
    c=a+b

N=int(input())
List=list(map(int,input().split()))
ans=0
div_conquer(0,N-1)