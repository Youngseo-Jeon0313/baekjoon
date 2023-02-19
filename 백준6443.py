import sys
from collections import deque
sys.setrecursionlimit(10**6)

si = sys.stdin.readline
N = int(si())

def dfs(current, li: list):
    if current == len(input):
        word_set.append("".join(li))
        return
    
    for i in range(len(input)):
        if visited[i] == 0:
            li.append(input[i]) # 추가
            visited[i] = 1 # 방문처리
            dfs(current + 1, li)
            li.pop() # 초기화
            visited[i] = 0 # 초기화
    return
for i in range(N):
    word_set = deque([]) 
    input = list(map(str, si().rstrip()))
    input.sort()
    visited = [0 for _ in range(len(input))]
    dfs(0, [])

    word_set = set(list(word_set))
    word_set=list(word_set)
    word_set.sort()
    for word in word_set:
        print(word)
        