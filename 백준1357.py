X, Y = map(int, input().split())
Rev_X=str(X)[::-1]
Rev_X = int(Rev_X)

Rev_Y=str(Y)[::-1]
Rev_Y = int(Rev_Y)

answer = int(str((Rev_X + Rev_Y))[::-1])

print(answer)



