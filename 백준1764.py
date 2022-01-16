n, m =map(int, input().split())
A,B=set(), set()
for i in range(n):
    s=input()
    A.add(s)
for i in range(m):
    s=input()
    B.add(s)
C=sorted(list(A & B))
print(len(C))
for i in range(len(C)):
    print(C[i])

#주로 set은 집합으로 사용
#그리고 중복제거 기능 시 사용
#set의 가장 큰 특징은 데이터의 위치와 순서가 없다는 것
#즉 indexing, slicing, sorting 등을 못 쓴다.