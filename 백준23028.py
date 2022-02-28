N,A,B=map(int,input().split())
flag=True
now=N
for i in range(10):
    MJ, GE=map(int,input().split())
    if i<N: continue
    MAX=6
    while MAX>0 and MJ>0 and A<66: A+=3; B+=3; MJ-=1; MAX-=1
    while MAX>0 and GE>0: B+=3; GE-=1; MAX-=1
    now+=1
    if now==8 and A>=66 and B>=130: flag=False;
    
if flag==True: print('Nae ga wae')
else: print('Nice')
'''
다 다녔는데도 학점을 못 채운 경우??
'''