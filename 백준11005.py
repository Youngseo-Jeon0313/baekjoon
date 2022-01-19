'''
10진법에서 B진법으로 변환해서 출력하는 문제!

'''
D={} #딕셔너리에다가 이제 어떤 수를 출력해야 할지를 넣을 예정
for i in range(10):
    D[i]=str(i)
for i in range(26):
    D[i+10]=chr(65+i)
'''
원래 십진수의 원칙은
1 2 3 4 5 6 7 8 9 a b c d  ... 이거라서 이렇게 넣어줌!

'''
n, b = map(int, input().split())
ans=[]
while 1:
    if n==0: break
    x=n%b
    ans.append(D[x])
    n //=b
print(''.join(ans[::-1]))