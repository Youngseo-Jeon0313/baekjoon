import sys
sys.setrecursionlimit(10**9)

N=int(input())
answer = float('inf')

def check(num):
    for i in range(1,len(num)//2+1): # 개수 
        if num[-i:]==num[-(i*2):-i]:
            return False
    return True

def dfs(num):
    global answer
    if len(num)==N:
        if check(num):
            print(num)
            exit()
    for i in '123':
        if check(num+i):
            dfs(num+i)

dfs('')
print(answer)