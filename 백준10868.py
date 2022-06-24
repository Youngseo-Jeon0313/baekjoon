
#10868
#세그먼트트리를 이용해서 최대값 / 최소값 구할거다!
import sys
import math
input=sys.stdin.readline

def init_min(node, start, end):
    if start==end:
        mintree[node]=leaf[start]
        return mintree[node]
    else:
        mintree[node]=min(init_min(node*2,start, (start+end)//2 ), init_min(node*2+1, (start+end)//2+1, end))
        return mintree[node]
#[start, end]는 지금 node가 어디를 포함하는 건지
#[left, right]는 우리가 목표하는 곳.!
def MIN(node, start, end, left, right):
    if left > end or right < start: return float('inf') #말도 안되는 것이 입력으로 들어옴
    if left <= start and end <= right: return mintree[node] #and인 거 잘 보자. 우리가 딱 구하고자 하는 것임!
    return min(MIN(node*2, start, (start+end)//2, left, right), MIN(node*2+1, (start+end)//2+1, end,left, right))

def init_max(node, start, end):
    if start==end:
        maxtree[node]=leaf[start]
        return maxtree[node]
    else:
        maxtree[node]=max(init_max(node*2,start, (start+end)//2 ), init_max(node*2+1, (start+end)//2+1, end))
        return maxtree[node]
#[start, end]는 지금 node가 어디를 포함하는 건지
#[left, right]는 우리가 목표하는 곳.!
def MAX(node, start, end, left, right):
    if left > end or right < start: return -1 #말도 안되는 것이 입력으로 들어옴
    if left <= start and end <= right: return maxtree[node] #and인 거 잘 보자. 우리가 딱 구하고자 하는 것임!
    return max(MAX(node*2, start, (start+end)//2, left, right), MAX(node*2+1, (start+end)//2+1, end,left, right))


n,m=map(int,input().split())
leaf=[]
mintree=[0]*3000000
maxtree=[0]*3000000

for _ in range(n):
    leaf.append(int(input().rstrip()))
init_min(1,0,n-1) #노드는 1부터 시작해서, 그리고 leaf는 0부터 따져서 트리 만들어가기!
init_max(1,0,n-1)


for _ in range(m):
    s,e=map(int,input().split())
    print(MIN(1,0,n-1,s-1,e-1))