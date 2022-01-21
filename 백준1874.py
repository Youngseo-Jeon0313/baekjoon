'''
망했다...
자꾸 시간초과 난다ㅠㅠㅠ
스택 하나에 입력된 수를 넣었다가 top이 입력한 수와 맞으면 pop하도록 하기


'''






import sys
input=sys.stdin.readline

n=int(input())
List=[]
startList=[]
endList=[]
for i in range(1,n+1):
    startList.append(i)
for j in range(1, n+1):
    endList.append(int(input()))

i=0
j=0

'''
start = / / / 4 5 6 7 8
end =   / / 6 8 7 5 2 1
List=   1 2 
'''

while True:
    if endList[i] in List:
        List.pop()
        print('-')
        i+=1
        if i==n:
            break
    else:
        if j==n:
            break
        List.append(startList[j])
        print('+')
        j+=1
        

