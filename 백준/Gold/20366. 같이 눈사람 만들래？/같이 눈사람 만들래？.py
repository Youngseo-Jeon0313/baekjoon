'''
만약 600개에서 4개의 쌍을 찾으면 
600C4
'''

#아이디어 신박 -> 세 용액 문제를 넘어 네 용액 문제이다!
N=int(input())
List=list(map(int,input().split()))
List=sorted(List)

#비교값 init
ans=float('inf')

for i in range(N-3):
    for j in range(i+3, N):
        #위에 i,j로 두 개를 구하고 그 안에서 left, right를 고를 예정
        left = i+1
        right= j-1
        # 비교값 init
        temp = float('inf')
        while left<=right:
            compare=(List[i]+List[j]-(List[left]+List[right]))
            if abs(compare)<ans:
                ans=abs(compare)
            if compare<0: #left+right을 더 작게 만들어야 함
                right-=1
            else:
                left+=1
print(ans)

'''
생각 ?
정렬했을 때 우리는 4개를 이용해서 2개씩 짝의 가장 minimum 합을 알 수 있다.
2 3 5 5 9
-> 2 (3 5) 5 
2 2 3 3 4 4
-> 2 (2 3) 3

'''