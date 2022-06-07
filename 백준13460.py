'''
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는가?
10번 이하로 움직여서 빼낼 수 없다면 -1 출력
'''
import sys
from copy import deepcopy



N,M=map(int,input().split()) #세로 가로
List=[]
for _ in range(N):List.append(list(input()))


def dfs(board,cnt):
    global ans
    if cnt==5:
        for i in range(N):
            for j in range(M):


