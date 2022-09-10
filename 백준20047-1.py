import sys
input=sys.stdin.readline

N=int(input())
before=input()
after=input()

one,two=map(int,input().split())

first_x=0; first_zero=0;
second_x=0; second_zero=0;
for i in range(N):
    if before[i]=='x': first_x+=1;
    if before[i]=='o': first_zero+=1
    if after[i]=='x': second_x+=1;
    if after[i]=='o': second_zero+=1
if first_x==second_x and first_zero==second_zero: flag=True
else: flag=False

if flag==False: print("NO"); exit()

DP=[[0 for _ in range(N)] for _ in range(3)]
#DP[i][0/1/2] i번째까지 0/1/2개 썼을 때 after[:i]까지 맞는 갯수의 최댓값


for i in range(N):
    if before[i]==after[i]:
        DP[0][i]=DP[0][i-1]+1
    if i>0 and before[i-1]==after[i]:
        DP[1][i]=max(DP[1][i],DP[0][i-1]+1)
    if i>1 and before[i-2]==after[i]:
        DP[2][i]=max(DP[2][i],DP[1][i-1]+1,DP[0][i-2]+2)
for j in range(3):
    print(*DP[j])
if DP[2][N-1]==N or DP[2][N-1]==N-1 or DP[2][N-1]: print("YES"); exit()
print("NO")

'''
3
oxo
xoo
1 2

4
oxoo
xooo
1 2

4
oxox
xoxo
1 3
'''