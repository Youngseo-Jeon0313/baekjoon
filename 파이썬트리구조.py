'''
파이썬에서 트리 구조를 class 생성자를 이용해서 구현해보자!
'''
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#파이썬에 처음부터 트리 구현
root=Node(10) #루트노드
root.left=Node(34) #루트노드 왼쪽에 달리는 노드
root.right=Node(89) #루트노드 오른쪽에 달리는 노드
root.left.left=Node(45)
root.left.right=Node(50)

#python에서 이진 트리 탐색
'''
트리를 만들었으면 가로질러 트리 요소를 인쇄해보자!! 순회!
순서는 위에서 아래로, 왼쪽에서 오른쪽으로 
'''
#선주문조회
def preorder(node):
    if node: #만약에 노드가 있다면
        print(node.data)
        preorder(node.left)
        preorder(node.right)

#순서 내 조회
'''
완전 맨 왼쪽에서부터 차례대로 오른쪽으로 가면서 확인하는'''
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
#주문 후 순회
'''
왼쪽 노드와 오른쪽 노드에서 재귀를 수행한 후 동일한 노드를 세 번째로 방문하면 해당 노드 인쇄
'''
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)
        