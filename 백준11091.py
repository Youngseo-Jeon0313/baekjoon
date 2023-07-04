N=int(input())
for _ in range(N):
    a=input()
    a=a.lower()
    ans=''
    arr=[0 for _ in range(26)]
    for i in a:
        if ord('a')<=ord(i)<=ord("z"):
            arr[ord(i)-ord('a')]+=1
    
    for j in range(26):
        if arr[j]<=0: ans+=(chr(j+ord('a')))
    if ans: 
        print('missing',ans)
    else:
        print('pangram')