# 이기면 20점 획득, 지면 15점 손실
N, P = map(int,input().split())
winpoint, losepoint, total = map(int,input().split())
dict = {}

flag=False
for _ in range(P):
    a,b = input().split()
    dict[a]=b

score = 0
for _ in range(N):
    person = input()
    if person in dict.keys() and dict[person]=='W':
        score += winpoint
    else:
        score -= losepoint
        score = max(score, 0)
    if score>=total: 
        flag=True

if not flag:
    print("I AM IRONMAN!!")
else:
    print("I AM NOT IRONMAN!!")
