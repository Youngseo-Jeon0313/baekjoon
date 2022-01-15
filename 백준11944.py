import sys
sys.setrecursionlimit(1000)

N, M =map(int,input().split())

List=list()

List.append(str(N))
List=List*N


if len(str(N))*N < M:
    print(str(N)*N)
else:
    print(str(N)*(M//len(str(N))), end='')
    for j in range(M%len(str(N))):
        print(str(N)[j], end='')

'''
런타임 에러
:너무 for문을 많이 돌면 그렇게 될 수 있음..
'''