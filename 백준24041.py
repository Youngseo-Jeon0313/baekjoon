N,G,K=map(int,input().split())
L=[]
must=[]
select=[]
for _ in range(N):
    a,b,c=map(int,input().split())
    if c==0: must.append([a,b])
    else: select.append([a,b])

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) //2
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    if array[mid] ==target:
        return mid
    #중간값의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, mid+1, end)


for 