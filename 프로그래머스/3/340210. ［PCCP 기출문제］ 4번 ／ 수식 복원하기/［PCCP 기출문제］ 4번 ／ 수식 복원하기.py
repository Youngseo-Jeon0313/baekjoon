answer=[]
def TenToN(num,N):
    num=int(num)
    res = ''
    while num:
        a,b = divmod(num,N)
        res = str(b)+res
        num = a
    return int(res or '0')

def NtoTen(N, num):
    N = int(N or '0')
    res = 0
    if len(str(N))==1:
        return N
    for i in range(len(str(N))):
        res += int(str(N)[i])*(num**(len(str(N))-1-i))
    return res

def solution(expressions):
    solveds=[]
    toBeSolveds=[]
    jinsooNums=[]
    
    for i in range(2,10):
        flag=True
        for expression in expressions:
            solvedList = expression.split(' ')
            numList = solvedList[0]+solvedList[2]+solvedList[-1]
            for num in numList: 
                if num=='X': continue
                if int(num)>=i: flag=False; break
        if flag: jinsooNums.append(i)       
                
    for expression in expressions:
        if 'X' in expression:
            toBeSolveds.append(expression)
        else:
            solveds.append(expression)
    jinsoos =[]
    
    for i in jinsooNums:
        flag=True
        for solved in solveds:
            solvedList = solved.split(' ')
            if solvedList[1]=='+':
                if NtoTen(solvedList[0],i)+NtoTen(solvedList[2],i)!=NtoTen(solvedList[-1],i): flag=False
            elif solvedList[1]=='-':
                if NtoTen(solvedList[0],i)-NtoTen(solvedList[2],i)!=NtoTen(solvedList[-1],i): flag=False
        if flag: jinsoos.append(i)

    for toBeSolved in toBeSolveds:
        possible_X=[]
        toBeSolvedList = toBeSolved.split(' ')
        for jinsoo in jinsoos:
            if toBeSolvedList[1]=='+':
                possible_X.append(TenToN(NtoTen(toBeSolvedList[0],jinsoo)+NtoTen(toBeSolvedList[2],jinsoo),jinsoo))
            elif toBeSolvedList[1]=='-':
                possible_X.append(TenToN(NtoTen(toBeSolvedList[0],jinsoo)-NtoTen(toBeSolvedList[2],jinsoo),jinsoo))
        if len(set(possible_X))==1:
            toBeSolvedList[-1]=str(possible_X[0])
        else:toBeSolvedList[-1]='?'
        answer.append(' '.join(toBeSolvedList))
    
    return answer