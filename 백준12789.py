n=int(input())
s=list(map(int, input().split()))
i=1
start=1

arr=[]

while s:
    if s[0]==start:
        s.pop(0)
        start+=1
    else:
        arr.append(s[0])
        s.pop(0)
    
    while arr:
        if arr[-1]==start:
            arr.pop()
            start+=1
        else:
            break


if not arr:
    print('Nice')
else:
    print('Sad')