# find 연산
def find(target):
    if target == parent[target]:
        return target
 
    # 경로 압축 최적화
    parent[target] = find(parent[target])
    return parent[target]
 
# union 연산
def union(a, b):
    a = find(a) #이거 빼먹지 않도록 주의ㅠㅠㅠ
    b = find(b)
 
    # 작은 루트 노드를 기준으로 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 
parent = [0, 1, 2, 3, 4, 5]
 
# 노드 3과 노드 5가 같은 집합인지 비교
# 출력 결과 : 다른 집합입니다!
if find(3) == find(5):
    print("같은 집합입니다!")
else:
    print("다른 집합입니다!")
 
# 노드 3과 노드 5를 union 연산(합침)
union(3, 5)
 
# 노드 3과 노드 5가 같은 집합인지 비교
# 출력 결과 : 같은 집합입니다!
if find(3) == find(5):
    print("같은 집합입니다!")
else:
    print("다른 집합입니다!")
#유니온 + 파인드