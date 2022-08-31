
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
for _ in range(N):
    x,y=map(int,input().split())
G=0; R=0; B=0;

for _ in range(M):
    v,w,c=input().split()
    if c=='R': R+=1
    elif c=='G':G+=1
    else: B+=1

A=0; N=0
while True:
    if G>0:A+=1; G-=1
    elif R>0: A+=1; R-=1 
    else: print('jhnan917'); break;
    if G>0: N+=1; G-=1
    elif B>0: N+=1; B-=1
    else: print('jhnah917');break;
