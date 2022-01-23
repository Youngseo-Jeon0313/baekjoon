'''
갑자기 2로 안나누어지는 구간을 찾을 것이다.
'''
n=int(input())
for i in range(64):

    if n%2==0:
        n//=2
    else:
        print(64-i)
        break