t=int(input())

'''
s[i]=chr(((ord(s[i]) - 65 + 26 - 13) % 26) + 65)

핵심은 A의 ord를 0으로 만든 다음에 이제 더해서 나머지!!
그걸로 해가지고 가져오는거.
'''


for i in range(t):
    a,b=map(int,input().split())
    s=list(input())
    for i in range(len(s)):
        s[i]=chr(((ord(s[i])-65)*a+b)%26+65)
    print(''.join(s))
        