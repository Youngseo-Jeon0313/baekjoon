'''
이렇게 된 문자열의 특징
1. (의 개수와 )의 개수가 똑같다.
2. 입력받을 ★때 )의 개수가 (의 개수를 넘어갈 수 없다.'''

t=int(input())
for i in range(t):
    s = list(input())
    l, r= 0, 0
    arr=[]
    flag = True #True False값으로 바꿀 때 flag를 많이 씀
    for j in range(len(s)):
        if s[j] =='(':
            l+=1
            arr.append('(')
        else:
            r+=1
            if len(arr) ==0: 
                flag =False 
            else:
                arr.pop() #아 arr에 넣고 빼면서 빼는 게 있어야 되는데 없다? 그러면 이제 flag를 False값으로 바꿔주기
    if l==r and flag ==True: print("YES")
    else: print('NO')
