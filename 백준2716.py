N=int(input())

'''
[]    
  
[[][[]]]
스택 -> [] 이 안에 [] 이거랑 [[]] 이게 있음
  [] depth 0  root가 a와 b로 갈라짐
[] [[]] depth 1  a가 두 개로 갈라지고 b가 c와 d로 갈라짐
    [] depth 2  그 중 하나, c가 두 개로 갈라짐 

depth를 우선 구한다.
0부터 시작
'''
for _ in range(N):
    a = input()
    ans = [0]
    stack = []
    depth = 0
    for i in a:
        #print(stack)
        if i=='[':
            depth+=1
            stack.append(('[',depth))
            
        elif i==']':
            x = stack.pop()
            depth -=1
            ans.append(x[1])
    
    print(2**max(ans))
    