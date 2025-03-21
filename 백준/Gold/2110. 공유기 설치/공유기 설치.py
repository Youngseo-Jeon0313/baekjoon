# 백준 2110

N, C = map(int,input().split())
List = []
for i in range(N):
    num = int(input())
    List.append(num)
List.sort()
left = 0; right =(List[-1]-List[0])*2

while left < right:
    mid = (right+left)//2
    #print(left, right, mid)
    temp = 1; pos = List[0]
    #일단 비교치를 위한 기준을 만든다.
    for i in List:
        if i-pos>=mid:
            temp+=1
            pos = i;
    #print(temp)        
    if temp<C: #범위를 좁힌다.
        right = mid
    else:
        left = mid+1
        answer = mid

print(answer)


'''

5 4
1
2
8
4
9

답 - 1
'''