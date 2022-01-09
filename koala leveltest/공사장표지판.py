#짝수일 때와 홀수일 때 좀 다름

line = int(input())

for i in range(1, line+1):
    if i==1 or i==line:
        print('*'*line,end='')
    else:
        for j in range(1, line+1):
            if j==1 or j==line: 
                print('*',end='')
            elif j==i or j==line+1-i: 
                print('*',end='')
            else:
                print(' ',end='')
    print()

