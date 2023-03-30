N=int(input())
List=[]
for _ in range(N):
    List.append(list(map(int,input().split())))
rank=[1 for _ in range(N)]
List1=sorted(List, key=lambda x:x[0])
List2=sorted(List,key=lambda x:x[1])
'''
몸무게와 키 모두 자기보다 큰 사람의 수 를 센다.
'''
for i in range(N):
    for j in range(N):
        if i==j: continue
        if List[j][0]>List[i][0] and List[j][1]>List[i][1]:
            rank[i]+=1

print(*rank)