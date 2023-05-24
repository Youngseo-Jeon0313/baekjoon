s=input()
M=0; O=0; B=0; I=0; S=0
for i in s:
    if i=='M': M=1
    elif i=='O': O=1
    elif i=='B': B=1
    elif i=='I': I=1
    elif i=='S': S=1
if M*O*B*I*S: print("YES")
else: print("NO")