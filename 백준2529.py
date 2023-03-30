n=int(input())
compare = list(input().split())

MAX=0
MIN=float('inf')

def back(ans,compare_num):
    global MAX, MIN;
    if len(ans) == n+1: # 배열의 길이를 확인
        MAX=max(MAX,int(''.join(str(x) for x in ans)))
        MIN=min(MIN,int(''.join(str(x) for x in ans)))
        return 
    for i in range( 10): # 1 ~ N 까지
        if i not in ans : # 중복 확인
            if compare[compare_num]=='<' and ans[-1]<i:
                back(ans+[i],compare_num+1)
            elif compare[compare_num]=='>' and ans[-1]>i:
                back(ans+[i],compare_num+1)

for i in range(10):
    back([i],0)

print(str(MAX).zfill(n+1))
print(str(MIN).zfill(n+1))