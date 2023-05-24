a,b,c=map(int,input().split())
res = max(b,a-b) * max(c,a-c)
print(4*res)