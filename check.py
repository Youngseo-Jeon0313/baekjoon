N=int(input())
Tree=[[] for _ in range(N+1)]
for i in range(N-1):
    parent,child=map(int,input().split())
    Tree[parent].append(child)
print(Tree[1])