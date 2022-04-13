'''
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
        b=''.join(map(str, letters[i]))
        a=''.join(map(str, letters_bitmasking))
        c=bin(int(a,2)&int(b,2))
        if int(c[2:])==int(b): sum+=1
    print(sum)



문자열의 빈칸을 채우는..

문자열.rjust(width,"0") #왼쪽에다가 0 채우기
'''

import sys
input =sys.stdin.readline
n,m=map(int,input().split())
wordList=[]
for _ in range(n):
    word=input().strip()
    bitmask=0
    for i in word:
        i=ord(i)-ord('a')
        bitmask |= (1 << i)
    wordList.append(bitmask)
bitmask2=0b11111111111111111111111111
for _ in range(m):
    x,what=input().strip().split()
    what=ord(what)-ord('a')
    if x=='1':
         bitmask2 &= ~(1<<what) #what을 2진수로 나타낸 것 중 1에 해당하는 것들을 제외 (0있는 것들만 있는 걸로 취급)
    else: 
        bitmask2 |= (1<<what) 
    count=0
    for y in wordList:
        if bitmask2 & y == y: count+=1
    print(count)




'''
wordlist=[]
word=input()
bitmask=0
for i in word:
    i=ord(i)-ord('a')
    bitmask |= (1<<i)
wordlist.append(bitmask)
#bin(bitmask) 0b1000100000010001
print(bin(bitmask))
'''
