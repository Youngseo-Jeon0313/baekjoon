#나누기는 위험하다!!! 출력초과!!!

import sys
input=sys.stdin.readline

N=int(input())
List=list(map(int,input().split()))
List_up=[];List_down=[]
ans_up=0; ans_down=0

for j in List:
    if j>=0: List_up.append(j)
    else: List_down.append(j)
sum_up=sum(List_up)
ans_up=sum_up*len(List_up)
ans_down=sum(List_down)
ans=ans_up+ans_down
if len(List_up)==0 or len(List_down)==0: print(ans); exit();

List_down.sort(reverse=True)
for i in range(len(List_down)):
    sum_up+=List_down[i]
    ans_up=sum_up*(len(List_up)+i+1)
    ans_down-=List_down[i]
    temp_ans=ans_up+ans_down
    if temp_ans>ans: ans=temp_ans

print(ans); exit();