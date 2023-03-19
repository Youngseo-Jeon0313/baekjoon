import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    before=input()
    after=input()
    flag=True
    ascii_list=[0 for _ in range(100)]
    for l in before:
        ascii_list[ord(l)-ord('a')]+=1
    for k in after:
        ascii_list[ord(k)-ord('a')]-=1
    # print(ascii_list)
    for i in ascii_list: 
        if i!=0: flag=False
    for i in range(N):
        if before[i]!=after[i]: 
            if i<K and N-i-1<K: flag=False; break;
    if flag: print("YES")
    else: print("NO")
