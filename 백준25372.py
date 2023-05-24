N=int(input())
for _ in range(N):
    pw=input()
    if 6<=len(pw) and len(pw)<=9: print('yes')
    else: print('no')