# import sys
# input=sys.stdin.readline

check=[-1 for _ in range(26)]
s=input()
for i in range(len(s)):
    word=s[i]
    if check[ord(word)-97]==-1: check[ord(word)-97]=i

print(*check)