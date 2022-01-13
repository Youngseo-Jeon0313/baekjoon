#시간초과 오류!!



files=int(input())
File=list(map(int, input().split()))
limit=int(input())

num=0

for i in range(files):
    if File[i]>0:
        while (File[i]>0):
            num+=1
            File[i]-=limit

print(num*limit)
