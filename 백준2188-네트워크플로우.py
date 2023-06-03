def BFS():
    global capacity
    global flow
    total = 0
    while(True):
        stack = [0]
        chk = True
        pre = [-1] * totalVertex
        while(len(stack) != 0 and chk ):
            value = stack.pop(0)

            for i in range(totalVertex):
                if( pre[i] >= 0  ):
                    continue
                if( capacity[value][i] - flow[value][i] > 0 ):
                    stack.append(i)
                    pre[i] = value
                    if( i == totalVertex - 1 ):
                        chk = False
                        break

        if( pre[totalVertex-1] == -1 ):
            break
        temp = totalVertex - 1
        while( temp != 0):
            flow[pre[temp]][temp] = 1
            flow[temp][pre[temp]] = -1
            temp = pre[temp]
        total += 1
    return total


def DFS():
    global capacity
    global flow
    total = 0
    while (True):
        stack = [0]
        chk = True
        pre = [-1] * totalVertex
        while (len(stack) != 0 and chk):
            value = stack.pop()

            for i in range(totalVertex):
                if (pre[i] >= 0):
                    continue
                if (capacity[value][i] - flow[value][i] > 0 ):
                    stack.append(i)
                    pre[i] = value
                    if (i == totalVertex - 1):
                        chk = False
                        break

        if (pre[totalVertex - 1] == -1):
            break

        temp = totalVertex - 1
        while (temp != 0):
            flow[pre[temp]][temp] = 1
            flow[temp][pre[temp]] = -1
            temp = pre[temp]
        total += 1
    return total


if __name__ == "__main__":


    N,M = input().split()
    N,M = int(N),int(M)

    cowArray = [[]] * N
    for i in range(N):
        cowArray[i] = [int (k) for k in input().split()]


    totalVertex = N+M+2

    flow = [[0]*totalVertex for i in range(totalVertex)]
    capacity = [[0]*totalVertex for i in range(totalVertex)]

    for i in range(N):
        capacity[0][i+1] = 1
    for i in range(M):
        capacity[-2 - i][-1] = 1
    for i,j in enumerate(cowArray):
        for k in range(j[0]):
            capacity[i+1][j[k+1]+N] = 1

    print(BFS())
#   print(BFS())