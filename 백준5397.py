
n=int(input())
for _ in range(n):
    stack=[]
    str=input()
    cursor=0
    for i in str:
        it i!='<'
        if i=='<':
            if cursor!=0:
                cursor-=1
        elif i=='>':
            if cursor!=len(stack):
                cursor+=1
        elif i=='-':
            if cursor!=0:
                stack.pop(cursor-1)
                cursor-=1
        else:
            stack.insert(cursor,i)
            if cursor!=len(stack):
                cursor+=1
        if cursor>len(stack):cursor=len(stack)
        if cursor<0: cursor=0
    print("".join(stack))