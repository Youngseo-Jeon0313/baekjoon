H,M,D=map(int,input().split())
h,m,d=map(int,input().split())
if m>M or (m==M and d>=D): print(h-H)
else: print(h-H-1)
print(h-H+1)
print(h-H)