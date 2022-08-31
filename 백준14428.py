import sys
input=sys.stdin.readline

#트리 만들기
def init(node, start, end):
    if start==end:
        tree[node]=[leaf[start],start+1]
        return tree[node]
    else: 
        tree[node]=min(init(node*2,start,(start+end)//2 ),init(node*2+1, (start+end)//2+1, end))
        return tree[node]
def search(node, start, end, left, right):
    if left > end or right < start: return [float('inf'), float('inf')] #범위를 벗어날 경우 최대를 줘야 min에서 걸러짐
    if left <= start and end <= right: return tree[node] #딱 구하고자 할 경우.
    return min(search(node*2, start, (start+end)//2, left, right), search(node*2+1, (start+end)//2+1, end,left, right))

def update(node, start, end, index, diff):
    if index < start or index > end: #해당 노드를 따라 밑으로 한 칸 내려갔을 때 해당하는 쪽이 아닐 경우
        return float('inf')
    if start==end:
        tree[node]=[diff,index+1] #값 바꿔주기
        return
    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)
        tree[node]= min(tree[2*node],tree[2*node+1]) #그 다음에 처리


N=int(input())


tree=[[] for _ in range(N*4+1)]
leaf=list(map(int,input().split()))

init(1,0,N-1) #노드 맨위를 1로 해서 만들어 나가기!!

#print(tree)

M=int(input())
for _ in range(M):
    a,b,c=map(int,input().rstrip().split())
    if a==1:
        b=b-1
        diff=c
        update(1,0,N-1,b,diff)
        #print(tree)
    elif a==2:
        print(search(1,0,N-1,b-1,c-1)[1])

