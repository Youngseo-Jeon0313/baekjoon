import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

N=int(input())
before=input()
after=input()

one,two=map(int,input().split())
newbefore=''
for i in range(N):
    if i==one or i==two:continue
    newbefore+=before[i]

#인자: 현재 어디, 몇개가 맞니, cnt(몇 개 썼는가), 
def dfs(index,correct,cnt):
    #print(index,correct,cnt)
    if correct==N:
        if cnt==2: return 1
        else: return 0

    ret=0

    if index<N-2 and newbefore[index]==after[correct]: ret=max(ret,dfs(index+1,correct+1,cnt))
    if cnt==0 and after[correct]==before[one]: ret=max(ret,dfs(index,correct+1,cnt+1))
    if cnt==1 and after[correct]==before[two]: ret=max(ret,dfs(index,correct+1,cnt+1))

    return ret
if dfs(0,0,0): print("YES")
else: print("NO")


'''
3
oxo
xoo
1 2

4
oxoo
xooo
1 2

4
oxox
xoxo
1 3

4
xxxo
oxxx
1 3
NO
'''