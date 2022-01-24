N,M=map(int, input().split())
S=[]
for i in range(N):
    S.append(list(input()))
Series=[]
for i in range(N-7):
    for j in range(M-7):#시작이 되는 것들
        a=[S[y][j:j+8] for y in range(i, i+8)]
        Series.append(a)
NUM=[]
for i in Series:
    #(0,0)을 Black으로 지정해줬다고 하자
    num=0
    for x in range(8):
        for y in range(8):
            if (x+y)%2==0:
                if i[x][y]=='B':
                    continue
                else:
                    num+=1#다시 칠해야 함
            else:
                if i[x][y]=='W':
                    continue
                else:
                    num+=1
    NUM.append(num)
for i in Series:
    #(0,0)을 Black으로 지정해줬다고 하자
    num=0
    for x in range(8):
        for y in range(8):
            if (x+y)%2==0:
                if i[x][y]=='W':
                    continue
                else:
                    num+=1#다시 칠해야 함
            else:
                if i[x][y]=='B':
                    continue
                else:
                    num+=1
    NUM.append(num)

print(min(NUM))