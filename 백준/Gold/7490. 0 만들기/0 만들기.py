N = int(input())


def backtracking(arr, expression, start, M):
    if eval(expression) == 0 and start==M: # 배열의 길이를 확인
        ret=''.join(arr)
        ans.append(ret)
        return ret
    if start>M: return
    for i in ['+','-','']: # 1 ~ N 까지
        if i=='':
            backtracking(arr+[' '+str(start+1)], expression+i+str(start+1), start+1, M)
        else:
            backtracking(arr+[i+str(start+1)], expression+i+str(start+1), start+1, M)
            
for _ in range(N):
    ans = []
    M = int(input())
    backtracking(['1'], "1", 1, M)
    ans=sorted(ans)
    for i in ans: print(i)
    print()



      
