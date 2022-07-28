import sys
input=sys.stdin.readline

def binary_search(array, target, start, end):
    mid = (start+end) //2
    if start==end: return start
    if (array[mid] < target and array[mid+1] > target) or array[mid]==target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid)
    #중간값의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    elif array[mid] < target:
        return binary_search(array, target, mid, end)


N,K=map(int,input().split())
tree=list(map(int,input().split()))
tree=sorted(tree)
prefixsum=[]
for i in range(len(tree)):
    if i==0: prefixsum.append(tree[i])
    else:
        prefixsum.append(prefixsum[-1]+tree[i])
# print(prefixsum)
for _ in range(K):
    a=int(input())
    #이분탐색을 이용해서 들어가야할 자리 찾기
    if a>=tree[-1]:index=N
    elif a<tree[0]:index=0
    else:index=binary_search(tree,a,0,N-1)+1 #0 4
    # print('인덱스' ,index)
    if index==0:
        print(prefixsum[-1]-N*a)
    else:
        print(abs(a*index-prefixsum[index-1]+prefixsum[-1]-prefixsum[index-1]-a*(N-index)))


