import sys
# input=sys.stdin.readline
'''
경기 진행 도중 누군가가 
$2$점 앞서게 되면 경기가 종료되며 이후의 라운드는 진행하지 않는다.

'''
n=int(input())
D=0; P=0
for i in range(n):
    a=input()
    # print(a)
    if a=='D': D+=1;
    else: P+=1
    if D+2<=P or P+2<=D: break;
print(D,":",P,sep='')