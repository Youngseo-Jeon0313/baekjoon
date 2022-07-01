import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

N=int(input()) #노드의 개수
contents=list(map(int,input().split())) #1번부터 N번까지의 노드 속 적힌 정수 나열
Tree=[[] for _ in range(N+1)]
for i in range(N-1):
    parent,child=map(int,input().split())
    Tree[parent].append(child)

def checkstructure(num):
    #재귀함수로 구현한다. 자식노드의 형제/ ..쭉쭉쭉 그 형제들의 수가 다 동일해야 함
    store=[]
    if Tree[num] :  
        compare=len(Tree[Tree[num][0]])
        if compare!=0:
            for i in Tree[num]:
                if len(Tree[i])!=compare: #맨 밑까지 확인이 안되었는데 다른 게 나왔으면:
                    return False
                store.append(i)
    for i in store:
            checkstructure(i)
    return True

def checkcontents(arr):
    store=[]
    string=[]
    if len(arr)!=0:
        for i in arr:
            if Tree[i]:
                for j in Tree[i]:
                    store.append(j)
            string.append(contents[i-1])
        if string!=string[::-1]:
        #맨 밑까지 확인이 안되었는데 다른 게 나왔으면
            return False
        checkcontents(store)
    return True

ans=[]
for i in range(1,N+1):
    if checkstructure(i):
        if checkcontents(Tree[i]):
            ans.append(i)

print(len(ans))
print(*ans)


