N,A,B=map(int,input().split())
flag=True
for i in range(10):
    MJ, GE=map(int,input().split())
    MAX=6
    while MAX>0 and (MJ>0 or A<66): A+=3; B+=3; MJ-=1; MAX-=1
    while MAX>0 and (GE>0 or B<130) : B+=3; GE-=1; MAX-=1
    N+=1;
    if N<=8 and A>=66 and B>=130: print('Nice'); exit(); flag=False;

if flag==True: print('Nae ga wae')
'''
다 다녔는데도 학점을 못 채운 경우??
'''