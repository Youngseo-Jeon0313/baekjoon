'''
너무 똑똑하다...
어떻게 이런 문제를 만들어냈지..????

분할정복!!!!
'''

# num=1
# N=int(input())
# inorder=list(map(int,input().split()))
# postorder=list(map(int,input().split()))
# where=[-1]*(N+1) #inorder 속 숫자들은 어차피 다 다르다. 그들이 있는 위치를 [숫자]=어디 로 표시해줄 수단
# for i in range(N):
#     where[inorder[i]]=i

# def preorder(left_root,right_root,root):
    
#     print(postorder[root-1]) #3(postorder[3-1]) #1(postorder[1-1] #2(postorder[2-1])
#     #그 안에서 왼쪽 root로 가기
#     if left_root-1==-1 or where[left_root]==-1: return
#     preorder(where[left_root],left_root-1,left_root) # 0  0  1 # -1 -1  0
#     #그 안에서 오른쪽 root로 가기

#     preorder(where[right_root],right_root-1,right_root) #  1 1 2 # 0 0 1
    
    

# preorder(where[N-1],N-1,N) # 1 2 3


'''

8
2 1 4 3 5 7 6 8
2 1 3 4 7 8 6 5
'''

import sys
sys.setrecursionlimit(10**6)
N=int(input())
inorder=list(map(int,input().split()))
postorder=list(map(int,input().split()))
pos=[0]*(N+1)
for i in range(N):
    pos[inorder[i]]=i

def preorder(instart,inend,poststart,postend):
    if instart>inend or poststart>postend: return
    root=postorder[postend]
    print(root,end=" ")
    left=pos[root]-instart #왼쪽 인자 개수 #4개 #3개
    right=inend-pos[root] #오른쪽 인자 개수 #4개
    preorder(instart,instart+left-1,poststart,poststart+left-1) #0 3 0 3
    preorder(inend-right+1,inend,postend-right,postend-1)#4 7 4 7

preorder(0,N-1,0,N-1)