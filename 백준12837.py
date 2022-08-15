import sys
input=sys.stdin.readline

#트리 만들기
def init(node, start, end):
    if start==end:
        tree[node]=leaf[start]
        return tree[node]
    else:
        tree[node]=init(node*2,start, (start+end)//2 )+ init(node*2+1, (start+end)//2+1, end)
        return tree[node]
#[start, end]는 지금 node가 어디를 포함하는 건지
#[left, right]는 우리가 목표하는 곳.!
def subSum(node, start, end, left, right):
    if left > end or right < start: return 0 #말도 안되는 것이 입력으로 들어옴
    if left <= start and end <= right: return tree[node] #and인 거 잘 보자. 우리가 딱 구하고자 하는 것임!
    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2+1, (start+end)//2+1, end,left, right)

def update(node, start, end, index, diff):
    if index < start or index > end: #해당 노드를 따라 밑으로 한 칸 내려갔을 때 해당하는 쪽이 아닐 경우
        return
    tree[node]+=diff
    if start != end:
        #이제 자식 노드들도 diff만큼 더해주기 위해서 재귀적호출을 해주는 부분
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

N,Q=map(int,input().split())
leaf=[]
tree=[0]*(4*(N+1))

for _ in range(N+1):leaf.append(0) #리프노드

init(1,0,N-1) #노드 맨위를 1로 해서 만들어 나가기!!

for _ in range(Q):
    a,b,c=map(int,input().split())
    if a==1:
        b=b-1
        diff=c
        leaf[b]+=diff
        update(1,0,N-1,b,diff)
    elif a==2:
        print(subSum(1,0,N-1,b-1,c-1))
    # print('leaf:', leaf)
    # print('tree:',tree)