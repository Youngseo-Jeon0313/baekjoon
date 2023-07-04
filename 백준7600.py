while True:
    a=input()
    if a=='#': break;
    a=a.lower()
    ans=0
    arr=[0 for _ in range(26)]
    for i in a:
        if ord('a')<=ord(i)<=ord("z"):
            arr[ord(i)-ord('a')]+=1
    
    for j in range(26):
        if arr[j]>0: ans+=1
    print(ans)