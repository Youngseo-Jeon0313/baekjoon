import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())
index=1
answer=0
game=0
while N>1:
    game+=1
    N//=2
while True:
    if K-(2**index)>=0: answer+=1; index+=1;
    else:
        if M>0: M-=1; index+=1; answer+=1 
        else: 
            break;

print(min(game,answer))