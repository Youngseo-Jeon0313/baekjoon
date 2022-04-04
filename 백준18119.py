letters=[]
letters_bitmasking=[0]*26

N,M=map(int,input().split())
for _ in range(N): letters.append(input())
for i in letters:
    for j in i:
        letters_bitmasking[ord(j)-26]=1
for _ in range(M):
    o,x=input().split()
    if o=='1': letters_bitmasking[ord[x]-26]=0
    else: letters_bitmasking[ord[x]-26]=1
    sum=0
    for i in letters:
        for j in i:
            if letters_bitmasking[ord(j)-26]==1:continue
