List = list(map(int, input().split()))
n = min(List)
while True:
    cnt=0
    for i in range(5):
        if n%List[i] == 0:
            cnt += 1
    if cnt>2:
        print(n)
        break
    n+=1