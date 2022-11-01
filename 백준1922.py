import sys
input =sys.stdin.readline

V=int(input())
E=int(input())
root = [i for i in range(V+1)]
Elist=[]

for _ in range(E):
    start,end,val=map(int,input().split())
    Elist.append([val,start,end])

Elist.sort()

def find(x):
    if x!= root[x]:
        root[x]=find(root[x])
    return root[x]

answer = 0
for w, s, e in Elist:
    sRoot= find(s)
    eRoot = find(e)
    if sRoot!=eRoot:
        answer+=w
        if sRoot > eRoot:
            root[sRoot] = eRoot
        else:
            root[eRoot] =sRoot

print(answer)
