t=int(input())

for i in range(t):
    List=[]
    Check=[]
    s=list(input().split())
    while True:
        line=input()
        if line=='what does the fox say?':
            break
        L=list(line.split())
        Check.append(L[2])
    for i in s:
        if i not in Check :
            List.append(i)
    print(' '.join(List))