x,y=map(int,input().split())
month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
days=0
for i in range(1,x):
    days+=month[i]
days+=y-1
# print(days)
ans=["MON","TUE","WED","THU","FRI","SAT","SUN"]
print(ans[days%7])