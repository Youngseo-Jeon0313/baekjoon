import sys
input=sys.stdin.readline
def check(x):
    for i in range(x):
        if col[x]==col[i] or abs(col[i]-col[x])==x-i: 
        #+ 모양이나 X 모양 중 해당하는 게 있으면 안된다.
            return False
    return True

def dfs(x):
    global res #전역변수로 할당
    if x==n: #마지막 행에 도달하면
        res+=1 #오키 잘했어 하면서 경우의 수 하나를 찾은 거임
    else:
        for i in range(n):
            col[x]=i #x열의 행은 i라고 하면
            if check(x):
                dfs(x+1)
n=int(input())
res=0
col=[0]*n


dfs(0)
print(res)