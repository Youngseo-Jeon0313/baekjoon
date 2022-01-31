import sys
input=sys.stdin.readline

def go(depth):
    if depth==m:
        print(' '.join(map(str,arr)))
        return

    for i in range(len(L)):
        if depth==0 or arr[-1]<=L[i]:
            arr.append(L[i])
            go(depth+1)
            arr.pop()

n,m=map(int, input().split())
L=list(set(list(map(int,input().split()))))
L.sort()
arr=[]
go(0)