import sys
input=sys.stdin.readline

H,W,N,M=map(int,input().split())
sero=H//(N+1)
sero_one=0
garo_one=0
if H%(N+1)>0:
    sero_one = 1
garo=W//(M+1)
if W%(M+1)>0:
    garo_one = 1
print((sero+sero_one)*(garo+garo_one))
