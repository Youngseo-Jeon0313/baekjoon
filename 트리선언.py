'''
이 문제에서 내가 간과한 거는 기본적으로 여기서
그 크기순서대로 들어가는 게 아니다ㅠㅠㅠ
'''
class Tree:
    def __init__(self,val=None) : #만약 Tree(30)이렇게 해주면 val에 자동으로 들어간다.
        if val!=None: self.val=val
        else: self.val = None
        self.left = None
        self.right = None

    def insert(self, val): #기존 트리에 노드 삽입
        if self.val :
            if val < self.val:
                if self.left is None: #밑으로 더 내려가
                    self.left = Tree(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Tree(val)
                else:
                    self.right.insert(val)
        else: self.val=val #root노드에 그냥 넣어준다.

    def printValues(self): #왼쪽에서 중앙, 마지막으로 오른쪽에서 값을 인쇄하는 함수
        print(self.val)   
        if self.left :
            self.left.printValues()
        if self.right:
            self.right.printValues()

N=int(input())
in_order=list(map(int,input().split()))
post_order=list(map(int,input().split()))
tree=Tree()
for i in post_order:
    tree.insert(i)
tree.printValues()