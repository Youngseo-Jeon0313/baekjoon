'''
EOF를 쓰는 경우는
우리가 몇 줄 입력받을지를 모를 때 사용한다!

'''


s=''
while True:
    try:
        line=input()
        s += line
    except EOFError:
        break
arr = list(map(int, s.split(',')))
print(sum(arr))