from turtle import hideturtle


N=int(input())

T=tuple(map(int, input().split()))
hit = 0

for i in range(N):
    if T[i]!=i+1:
        hit+=1

print(hit)