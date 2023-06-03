n=int(input())
a,b,c,d,e=0,0,0,0,0;
for _ in range(n):
    x,y=map(int,input().split())
    if x>0 and y>0: a+=1
    elif x>0 and y<0: d+=1
    elif x<0 and y>0: b+=1
    elif x<0 and y<0: c+=1
    else: e+=1
print("Q1: {}".format(a))
print("Q2: {}".format(b))
print("Q3: {}".format(c))
print("Q4: {}".format(d))
print("AXIS: {}".format(e))