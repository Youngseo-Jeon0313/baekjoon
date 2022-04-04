
import sys
input=sys.stdin.readline


letters_bitmasking=[0]*26
N,M=map(int,input().split())
letters=[[0]*26 for _ in range(N)]
for i in range(N): 
    a=input().rstrip()
    for j in a:
        letters[i][ord(j)-97]=1
        letters_bitmasking[ord(j)-97]=1


for _ in range(M):
    o,x=input().split()
    if o=='1': letters_bitmasking[ord(x)-97]=0
    else: letters_bitmasking[ord(x)-97]=1
    sum=0
    for i in range(N):
        if bin(''.join(map(str,letters[i])) & ''.join(map(str, letters_bitmasking))) == bin(''.join(map(str, letters[i]))): sum+=1
    print(sum)
            