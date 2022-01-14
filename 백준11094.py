
'''
    N=int(input())
List=list()
for i in range(N):
    a=input()
    List.append(a.split())
    if List[0]=='Simon' and List[1]=='says':
        for i in range(2, len(List-1)):
            print(List[i],end=' ')
        print(List[i+1])

착각하지 말자. list에 그냥 다 갖다 넣는 방법도 가능
list에 글자를 하나씩 다 잘라서 갖다 넣는 거 생각하지 말고
그냥 일단 넣고 꺼낼 때 그냥 가지고 나오면 됨

'''

t=int(input())
S=list('Simon says')
for i in range(t):
    arr = list(input())
    if arr[:10] == S:
        print(''.join(arr[10:]))