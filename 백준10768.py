A=int(input())
B=int(input())

if A<2:
    print('Before')
elif A==2:
    if B<18:
        print('Before')
    elif B==18:
        print('Special')
    else:
        print('After')
else:
    print('After')