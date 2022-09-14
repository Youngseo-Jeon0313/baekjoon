import sys
input=sys.stdin.readline



N=int(input())
for _ in range(N):
    Dict={}

    ans=0
    num=int(input())
    s=list(map(int,input().split()))
    s.sort()
    for i in s:
        Dict[i]=i
    for i in range(num):
        for j in range(i+1,num):
            if (s[i]+s[j])/2 in Dict:
                #print(s[i],s[j],(s[i]+s[j])//2)
                ans+=1
    print(ans)

'''
1
7
1 5 3 2 8 7 4

'''