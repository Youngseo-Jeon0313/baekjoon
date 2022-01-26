n=int(input())

List=[]
List.append(list(input())) 
#일단 맨 처음에 넣는 것이 기준이된다.
for i in range(n-1):
    a=input()
    List.append(a)
    for j in range(len(a)):
        if List[0][j]!=a[j]:
            List[0][j]='?'
print(''.join(List[0]))
