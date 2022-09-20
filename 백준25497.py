import sys
input=sys.stdin.readline

N=int(input())
s=input()
ans=0
index=0
stack=[]
while True:
    if index==N: break;
    if s[index]=='L':
        stack.append('L')
    elif s[index]=='R':
        if len(stack)>0:
            while len(stack)>0 :
                x=stack.pop()
                if x=='L':
                    ans+=1; break;
    elif s[index]=='S':
        stack.append('S')
    elif s[index]=='K':
        if len(stack)>0:
            while len(stack)>0:
                x=stack.pop()
                if x=='S':
                    ans+=1; break;
    else:
        ans+=1
    index+=1
    
print(ans)