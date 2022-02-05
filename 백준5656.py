i=0
while True:
    i+=1
    a,b,c=input().split()
    if b=='E':
        break
    if a==c:
        if b=='==' or b=='>=' or b=='<=':
            print('Case {0}: true'.format(i))
        else:
            print('Case {0}: false'.format(i))
    elif int(a)>int(c):
        if b=='>' or b=='>=' or b=='!=':
            print('Case {0}: true'.format(i))
        else:
            print('Case {0}: false'.format(i))
    elif int(a)<int(c):
        if b=='<' or b=='<=' or b=='!=':
            print('Case {0}: true'.format(i))
        else:
            print('Case {0}: false'.format(i))
