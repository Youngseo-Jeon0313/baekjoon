import sys
input=sys.stdin.readline

n=int(input())
chapters=list(int(input()) for _ in range(n))

ans=0
chapter_cnt=0

if n==1:pass

while chapter_cnt < n:
    left_minute=30
    while left_minute >0:
        if (left_minute>chapters[chapter_cnt]):
            ans+=1
            left_minute -= chapters[chapter_cnt]
            chapter_cnt+=1

            if chapter_cnt >=n:
                break
        elif left_minute*2 >=chapters[chapter_cnt]:
            ans+=1
            chapter_cnt+=1
            break
        elif chapters[chapter_cnt]>left_minute*2:
            chapter_cnt+=1
            break
print(ans)