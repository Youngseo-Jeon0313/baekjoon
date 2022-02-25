import math
'''
브루트포스 알고리즘
겁나 고지식한!!
수학적으로 풀이하려고 하지 말고 그냥
break / continue, while문을 써서 그냥 제한을 걸어주고
무한대로 돌리기
'''
N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]
Jegob=[]

def jegob(n):
    if int(math.sqrt(n))**2==n: return True
    return False

def brute_force(r,c): #무조건 밑/오른쪽으로 가고, jegob판단 시 뒤집은 것도!
    #step을 정하기 위한..
    for i in range(-N,N):
        for j in range(-M,M):
            if i==0 and j==0: continue #무시
            step=0 #초기 step 크기
            x=r; y=c #while문을 돌려주기 위해 따로 저장
            String=''
            while 0<=x<N and 0<=y<M:
                String+=arr[x][y]
                step+=1
                x=r+step*i; y=c+step*j
                if jegob(int(String)):Jegob.append(int(String))

for i in range(N):
    for j in range(M):
        brute_force(i,j)

if len(Jegob)==0: print(-1); exit()
print(max(Jegob))