m,n,w,h  = map(int,input().split())
List = list(map(int,input().split()))
working_duty = list(map(int,input().split()))

# 사람들이 일하는 시간들 기록
first_work_day = [[] for _ in range(m)] 

flag=True

worker = 0
for i in range(n):
    if working_duty[i]:
        while working_duty[i]:
            if first_work_day[worker]:
                if first_work_day[worker][-1]+w>=i-h:
                    print(-1); exit()
            first_work_day[worker].append(i)
            #worker를 쓴다.
            if i+w>n: 
                print(-2); exit()
            for j in range(i,i+w):
                working_duty[j]-=1
            worker = (worker+1)%m

if flag:
    print(1)
    for i in range(m):
        print(i, *first_work_day[i])
else:
    print(-1)