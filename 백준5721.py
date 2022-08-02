import sys
input=sys.stdin.readline
'''
생갹회로..
일단 완전탐색으로 가능할까?? bfs의 끼미가 보인다.. 8단계 뿐이므로 칸들을 다 돌면서 확인하면서 최적의 경우를
찾아내면 되지 않을까??
이렇게 되면 시간복잡도가
MXN(칸들의 수)X2XNXN(하나 탐색할 때 위행/아래행/왼쪽/오른쪽 탐색)
|
|
그러면 너무 많아진다. 그러면 하나 탐색할 때 드는 시간복잡도를 줄일 수 있는데,
위행, 아래행을 어차피 다 없애는 거니까 그걸 누적합으로 표현해서 가져간다.
누적합은 어떤 구간 안에서의 일정한 규칙이 있어야 하는데 위에 꺼는 행이랑 열이 일정한 규칙으로
나타나지 않아서 풀 수 없음
|
|
우리가 원하는 테이블을 만들어본다. 8단계를 거칠 때마다 가장 큰 '크게 뺄 수 있는 박스는 뭐냐'로
계속 추적해나갈 수 있다.
결국 DP...
'''



while True:
    ans=0
    M,N=map(int,input().split())
    if M==0 and N==0: break
    List=[]
    DP=[[0 for _ in range(N)] for _ in range(M)]

    for _ in range(M):
        a=list(map(int,input().split()))
        List.append(a)
    DP_row=[0 for _ in range(M)]
    
    for i in range(M): #한 개씩 가능한 행 먼저
        for j in range(N):
            if j==0:
                DP[i][j]=List[i][j]
            elif j==1:
                DP[i][j]=max(DP[i][j-1],List[i][j])
            else:
                DP[i][j]=max(DP[i][j-2]+List[i][j],DP[i][j-1])
            if j==N-1:
                DP_row[i]=DP[i][N-1]

    # print(DP_row)
    for k in range(M):
        if k==0: continue
        elif k==1:
            DP_row[k]=max(DP_row[k-1],DP_row[k])
        else:
            DP_row[k]=max(DP_row[k-2]+DP_row[k],DP_row[k-1])
    print(DP_row[M-1])
    