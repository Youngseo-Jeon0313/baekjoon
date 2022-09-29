import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    
    dict={'T':0,'i':1,'m':2,'u':3,'r':4}
    check=[0 for _ in range(5)]
    s=input()
    if n!=5: print("NO"); continue;
    for i in s: 
        if i in dict.keys():
            check[dict[i]]=1
    if 0 in check: print('NO')
    else: print('YES')