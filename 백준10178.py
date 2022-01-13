t=int(input())
for i in range(t):
    total, son=map(int, input().split())

    print('You get {0} piece(s) and your dad gets {1} piece(s).'.format(total//son, total%son))