import sys
input=sys.stdin.readline

G=int(input())

weight=[]
for i in range(1,100000):
    weight.append(i**2)
left=0; right=1
flag=False
while left<right:
    if weight[right]-weight[left]<=G:
        if weight[right]-weight[left]==G:
            flag=True
            print(right+1)
        right+=1
    else: 
        left+=1
if not flag: print(-1)


