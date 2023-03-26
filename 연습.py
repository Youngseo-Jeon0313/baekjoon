x0, N=map(int,input().split())
#규칙을 찾는다.
check={}
RULES=[]
count=0
flag=0
exit_flag=0
for i in range(1,15):
    # print(check)
    if i==N+1: print(x0); 
    if x0%2==0:
        x0=(x0//2)^6
    else:
        x0=(x0*2)^6
    if x0 in check.keys():
        if check[x0]>=1: exit_flag=1; 
        else: 
            if not flag: flag=i
            check[x0]+=1; RULES.append(x0); count+=1
    check[x0]=0
    if exit_flag: break;
# print('아',count)
# print(flag)
# print(RULES)
if len(RULES)>0:
    print(RULES[(N-(flag))%len(RULES)])
