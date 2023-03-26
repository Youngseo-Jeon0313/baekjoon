import sys
input=sys.stdin.readline

#결국 언젠가 자신이 출발했던 곳으로 되돌아오게 된다.

#격자 공간
w,h=map(int,input().split())
#초기 위치
p,q=map(int,input().split())

t=int(input())

#x와 y를 따로 보자!
x_rule=[]
y_rule=[]
for i in range(p,w+1):
    x_rule.append(i)
for i in range(w-1,-1,-1):
    x_rule.append(i)
for i in range(1,p):
    x_rule.append(i)

for j in range(q,h+1):
    y_rule.append(j)
for j in range(h-1,-1,-1):
    y_rule.append(j)
for j in range(1,q):
    y_rule.append(j)
# print(x_rule)
# print(y_rule)

print(x_rule[t%len(x_rule)], y_rule[t%len(y_rule)])
