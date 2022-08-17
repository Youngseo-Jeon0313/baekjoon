N=int(input())
List=input()
start=List[0]
flag=True
for i in range(N*2):
    if i%2==0 :
        if List[i]!=start: flag=False;
    else:
        if List[i]==start: flag=False
if flag==False: print('No')
else: print('Yes')