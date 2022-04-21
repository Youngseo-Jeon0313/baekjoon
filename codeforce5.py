import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    list=[]
    sum=0
    for _ in range(n): list.append(input())
    for i in range(n-1):
        for j in range(i+1,n):
            if list[i][0]==list[j][0] and list[i][1]!=list[j][1]: sum+=1
            elif list[i][0]!=list[j][0] and list[i][1]==list[j][1]: sum+=1
    print(sum)