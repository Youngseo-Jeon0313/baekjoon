---
description: 이분탐색
---

# binary\_search

\#정의

이분탐색이란  sorting 방법 중 하나로, 내가 찾고자하는 정해진 / 정해지지 않은 값을 찾고자 할 때 사용할 수있는 방법이다. 검색 범위를 줄여나가면서 원하는 데이터를 검색할 수 있다.

\#팁

?어떻게 이분탐색을 눈치채야 하는가?&#x20;

\-만약 떨어져 있는 arr 속에서 특정 값을 찾고자 할 때

\-1부터 N까지 수 중에서 어떤 게 문제 조건에 맞는지 찾고자 할 때

\#조건

* 주어진 배열은 정렬되어 있어야 한다. (오름차순 또는 내림차순)&#x20;
* 무한루프에 빠지지 않도록 mid값을 정해야 한다.(잊을 수 있음 주의)
* zerodivisionerror(시작점을 0으로 정하는 경우 나올 수 있음)  &#x20;

\#주코드&#x20;

```
start=1
end=N
arr=[1,2,3,4,5,8,0,14,26]

arr.sort() #만약 정렬이 되지 않았을 경우 직접 해야 한다. 
while start<=end:
    if arr[mid]==target:
        print(mid)
    elif arr[mid]<=target:
        start=mid+1
    else:
        end=mid-1
    mid=(start+end)/2
print(-1) #내가 찾고자 하는 값이 없을 경
    
```

{% tabs %}
{% tab title="백준1477" %}
```
'''
이진탐색: 검색 범위를 줄여나가면서 원하는 데이터를 검색하는 알고리즘
여기에서는 일단 고속도로 입구부터 출구까지 칸칸마다 있는 거니까
오름차순 정렬된 리스트로 나타낼 수 있고, 이 때 어디에따가 몇 개를 놔야 목표값인
'휴게소 없는 거리 중 최대'를 제일 크게 할 수 있을까를 정할 수가 있다.

그 목표값 자체를 이진탐색을 통해서 구한다.
굉장히 정밀하다. mid를 너무 극단적인 수치가 아닌가? 하고 의심하지 말 것. 
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
        left = mid+1 #간격을 넓히기 위해 옮기고 다시 돌아가
    else: #목표한 값이 나오거나 목표값 못 채웠을 경워
        answer = mid  #목표한 값 나왔을 경우 출력
        right = mid-1 #목표값 못 채웠을 때 간격 좁히기 위해 옮기고 다시 돌아가
        #여기서 굳이 left, right를 따로 줄이고 넓히는 이유는 left는 0에서 시작하고 right는 l-1에서 시작하니까 그거 - 등으로 오버해서 나오지 말라고
print(answer)
```
{% endtab %}

{% tab title="백준1654" %}

{% endtab %}

{% tab title="백준2805" %}

{% endtab %}
{% endtabs %}
