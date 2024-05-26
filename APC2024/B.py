N, P, Q = map(int,input().split())
Strawberries = list(map(int,input().split()))
Shinemuskets = list(map(int,input().split()))

flag = True
flag_list = []

if (P == Q):
    for i in range(N):
        if Strawberries[i] != Shinemuskets[i]:
            flag = False
            break
    if flag:
        print("YES")
        print(*[0]*N)
    else: print("NO")
    exit()

for i in range(N):
    if ((Strawberries[i]-Shinemuskets[i])%(Q-P) == 0 and (Strawberries[i]-Shinemuskets[i])//(Q-P) >= 0):
        flag_list.append((Strawberries[i]-Shinemuskets[i])//(Q-P))
        continue
    else:
        flag = False
        break
if flag: 
    print("YES")
    print(*flag_list)
else: print("NO")
