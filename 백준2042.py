import sys
input=sys.stdin.readline

#top down 형식으로 맨 위부터 노드를 하나씩 만들어줘서 leaf까지 도달하자
#재귀적 특징으로 나아감
#이진탐색트리의 특징을 생각한다면 이는 필연적/당연적임
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
        #이제 자식 노드들도 diff만큼 더해주기 위해서 재귀적호출을 해주는 부ㅜㅂㄴ
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

n,m,k=map(int,input().split())
leaf=[]
tree=[0]*3000000

for _ in range(n):leaf.append(int(input().rstrip()))

init(1,0,n-1) #노드 맨위를 1로 해서 만들어 나가기!!

for _ in range(m+k):
    a,b,c=map(int,input().rstrip().split())
    if a==1:
        b=b-1
        diff=c-leaf[b] # 6-3=3 바꾸려는 것의 차이를 구한다.
        leaf[b]=c #그 leaf노드를 바꿔준다.
        update(1,0,n-1,b,diff)
    elif a==2:
        print(subSum(1,0,n-1,b-1,c-1))