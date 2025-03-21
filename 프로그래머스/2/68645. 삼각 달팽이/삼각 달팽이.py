def solution(n):
    N=n
    real_answer = []
    answer = [['' for _ in range(n)] for _ in range(n)]
    turn = 0;
    x = 0; y = 0;
    num = 1
    while n>0:
        if turn % 3 == 0: # 아래로
            for i in range(n):
                answer[y][x]=num
                num+=1
                if i==n-1: x+=1
                else: y+=1
        elif turn % 3 == 1: # 오른쪽으로
            for i in range(n):
                answer[y][x]=num
                num+=1
                if i==n-1: x-=1;y-=1
                else: x+=1
        else: # 왼쪽 위로
            for i in range(n):
                answer[y][x]=num
                num+=1
                if i==n-1: y+=1
                else: x-=1;y-=1
        n-=1; turn+=1
    # print(answer)
    for i in range(N):
        for j in range(N):
            if answer[i][j]:
                real_answer.append(answer[i][j])
        
    # print(real_answer)
    return real_answer