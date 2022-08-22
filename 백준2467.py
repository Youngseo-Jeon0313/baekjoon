import sys
input=sys.stdin.readline

N=int(input())
Drinks=list(map(int,input().split()))
flag=False
#갑자기 양수가 되는 index를 저장
index=-1; #다 음수로 주어질 때 대비
for i in range(len(Drinks)):
    if Drinks[i]>=0: index=i; temp_index=i; break;
if index==-1: #다 음수로 주어진다면
    left=N-2; right=N-1;
elif index==0 or index==1: #다 양수
    left=0; right=1;
else:
    flag=True #아예 음수일 때나 아예 양수일 때도 체크해야 돼서
    left=index-1; right=index;
ans=float('inf')
ans_x=left; ans_y=right;
while left>=0 and right<N :
    temp_min=abs(Drinks[left]+Drinks[right])
    if ans>temp_min: ans_x=left; ans_y=right; ans=temp_min
    if left>0 and temp_min>abs(Drinks[left-1]+Drinks[right]):
        left-=1
    elif right<N-1 and temp_min>abs(Drinks[left]+Drinks[right+1]):
        right+=1
    else: left-=1
if flag==True:
    if temp_index>1: #음수가 최소 두 개 있음
        if ans>abs(Drinks[temp_index-1]+Drinks[temp_index-2]): ans_x=temp_index-2; ans_y=temp_index-1; ans=abs(Drinks[temp_index-1]+Drinks[temp_index-2])
    if N-temp_index>1: #양수가 최소 두 개 있음
        if ans>abs(Drinks[temp_index]+Drinks[temp_index+1]): ans_x=temp_index; ans_y=temp_index+1; ans=abs(Drinks[temp_index]+Drinks[temp_index+1])
    
print(Drinks[ans_x], Drinks[ans_y])
