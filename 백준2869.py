import sys

A,B,V=map(int,  sys.stdin.readline().split())
day=0


if ((V-A)%(A-B)==0):
    print(1+(V-A)//(A-B))
else:
    print(1+(V-A)//(A-B)+1)