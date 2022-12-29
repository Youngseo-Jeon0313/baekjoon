from collections import deque


T=int(input())
for _ in range(T):
    s=input()
    q=deque(['Y','e','s','Y','e','s'])
    for i in range(333):
        q.append('Y')
        q.append('e')
        q.append('s')
    
    index=0
    flag=False
    flag1=False
    if s[0] not in q: flag1=True;
    else:
        while index<len(s) and q:
            n=q.popleft()
            if n!=s[index] and flag==False: q.append(n);
            elif n!=s[index] and flag==True: flag1=True; break;
            else: flag=True; index+=1
    if flag1 or index<len(s): print("NO")
    else: print("YES")
        
    