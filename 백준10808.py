s=input()
arr=[0]*26
for i in range(len(s)):
    x=ord(s[i])-97
    arr[x]+=1
print(' '.join(map(str, arr)))