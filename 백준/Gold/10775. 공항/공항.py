import sys
input=sys.stdin.readline

def find(target):
    if target == airport[target] :
        return target
    else:
        airport[target]=find(airport[target])
        return airport[target]

def union(a, b):
    a = find(a) #이거 빼먹지 않도록 주의ㅠㅠㅠ
    b = find(b)
    if a < b: airport[b] = a
    else: airport[a] = b

G=int(input().rstrip()); P=int(input().rstrip())
airport = [port for port in range(G+1)]
ans=0
for i in range(1,P+1): #i는 비행기
    a=int(input())
    dest = find(a)
    if dest == 0 : break
    # airport[dest]=airport[dest-1]
    union(dest, dest-1)
    ans+=1
# print(airport)
print(ans)