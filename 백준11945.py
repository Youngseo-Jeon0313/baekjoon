N,M=map(int,input().split())
List=[]
for _ in range(N):
    List.append(input())
for i in List:
    print(i[::-1])