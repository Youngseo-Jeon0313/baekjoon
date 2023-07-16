import sys
input = sys.stdin.readline

def recursion(preorder, inorder):
    
    if not preorder:
        return

    node = preorder[0]
    idx = inorder.index(node)

    recursion(preorder[1:idx+1], inorder[:idx])
    recursion(preorder[idx+1:], inorder[idx+1:])
    print(node, end=' ')

t=int(input())
for _ in range(t):
    n=int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    recursion(preorder, inorder)
    print()