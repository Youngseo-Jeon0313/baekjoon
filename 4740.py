while True:
    a=input()
    if a=='***':
        break
    a=list(a)
    print(''.join(a[::-1]))