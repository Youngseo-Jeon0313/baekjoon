n=int(input())

while n>0:
    N=int(input())
    player1=0
    player2=0
    while N:
        N-=1
        a,b=input().split()
        if a=='R' and b=='S':
            player1+=1
        elif a=='S' and b=='R':
            player2+=1
        elif a=='S' and b=='P':
            player1+= 1
        elif a=='P' and b=='S':
            player2+=1
        elif a=='R' and b=='P':
            player2+=1
        elif a=="P" and b=='R':
            player1+=1

    if player1>player2:
        print('Player 1')
    elif player1<player2:
        print('Player 2')
    else:
        print('TIE')
    n-=1