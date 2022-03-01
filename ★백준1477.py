'''
이진탐색: 검색 범위를 줄여나가면서 원하는 데이터를 검색하는 알고리즘
여기에서는 일단 고속도로 입구부터 출구까지 칸칸마다 있는 거니까
오름차순 정렬된 리스트로 나타낼 수 있고, 이 때 어디에따가 몇 개를 놔야 목표값인
'휴게소 없는 거리 중 최대'를 제일 크게 할 수 있을까를 정할 수가 있다.

그 목표값 자체를 이진탐색을 통해서 구하는데,
맨 처음은 일단 left+right인 거다.(+mid 사용해서 풀이시작) 
굉장히 정밀하다. mid를 너무 극단적인 수치가 아닌가? 하고 의심하지 말 것. 
mid에서 정밀하게 왼쪽 오른쪽으로 한칸씩 옮긴다
'''


N,M,L=map(int,input().split())
arr=list(map(int,input().split()))
arr.append(0)
arr.append(L)
arr.sort()


#일단 왼쪽과 오른쪽을 결정
left=1
right=L-1
while left <= right:
    mid = (left+right)//2
    count = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > mid:
            count += (arr[i]-arr[i-1]-1)//mid
    if count>M: #목표한 값보다 크게 나오면
        left = mid+1 #간격을 넓히기위해 옮기고 다시 돌아가
    else: #목표한 값이 나오거나 목표값 못 채웠을 경워
        answer = mid  #목표한 값 나왔을 경우 출력
        right = mid-1 #목표값 못 채웠을 때 간격 좁히기 위해 옮기고 다시 돌아가
        #여기서 굳이 left, right를 따로 줄이고 넓히는 이유는 left는 0에서 시작하고 right는 l-1에서 시작하니까 그거 - 등으로 오버해서 나오지 말라고
print(answer)