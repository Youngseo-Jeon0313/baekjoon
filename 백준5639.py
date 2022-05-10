import sys
sys.setrecursionlimit(20_000)
input=sys.stdin.readline
class Node():
    def __init__(self, data): #Node만들기 그 안에 data / left 노드와 연결 / right 노드와 연결 넣기
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self): #바로 만들기!
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data) #root로 root.left.right ..이런식으로 간다
        return self.root is not None
        
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data) #맨 처음 만들 때 node는 딱 한 개 생긴다.
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                return
            else:
                _post_order_traversal(root.left) #재귀함수에서 입력값을 어떤 순서로 받느냐에 따라 다름
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)
bst=BinarySearchTree()
while True:
    try:
        bst.insert(int(input()))
    except: break

bst.post_order_traversal()