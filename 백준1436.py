import sys
input=sys.stdin.readline

N=int(input())
index=0
for i in range(200000000):
    if '666' in str(i): 
        index+=1
        if index==N: print(i); exit()
    