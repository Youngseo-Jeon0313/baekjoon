import sys
#파이썬 binary로 바꾸는 함수 bin()
Q = sys.stdin.readline()
Q=int(Q)
while Q:
    Q-=1
    a=int(sys.stdin.readline())
    t=int(bin(a)[2:]) #맨 앞에는 0b가 써지기 때문에 그거는 생략시키기 위해서
    if t&(-t) == a:
        print(1)
    else:
        print(0)


#이진수를 이용해서 푸는 것이 핵심!