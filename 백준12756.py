
A_attack, A_life=map(int, input().split())
B_attack, B_life=map(int, input().split())
while True:
    B_life -=A_attack
    A_life -=B_attack

    if B_life <=0 and A_life<=0:
        print("DRAW")
        break
    elif B_life <= 0:
        print('PLAYER A')
        break
    elif A_life <= 0:
        print('PLAYER B')
        break