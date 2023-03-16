# import sys
# input=sys.stdin.readline

def find(target, parent):
    if target == parent[target]:
        return target
    return find(parent[target])
 
def union(a, b, parent):
    a = find(a, parent) 
    b = find(b, parent)
    if a < b: parent[b] = a
    else: parent[a] = b

N=int(input())
parent1 = [i for i in range(N+1)]
parent2 = [i for i in range(N+1)]
parent3 = [i for i in range(N+1)]

M1,M2,M3=map(int,input().split())
invited_M1=[0 for _ in range(N+1)]
for _ in range(M1):
    a,b=map(int,input().split())
    invited_M1[a]=1; invited_M1[b]=1;
    union(a,b, parent1)
print(parent1)   

invited_M2=[0 for _ in range(N+1)]
for _ in range(M2):
    a,b=map(int,input().split())
    if a>b: a,b=b,a
    if parent2[b]>a : continue #이미 크다면 합치지마
    else:
        invited_M2[a]=1;  invited_M2[b]=1;
        parent2[a]=a; 
        union(a,b)
for i in range(N+1): 
    if not invited_M2[i] and invited_M1[i]:
        parent2[i]=i
        invited_M2[i]=0
print(parent2)

invited_M3=[0 for _ in range(N+1)]
for _ in range(M3):
    a,b=map(int,input().split())
    if a>b: a,b=b,a
    if parent3[b]>a : continue #이미 크다면 합치지마
    else:
        invited_M3[a]=1; invited_M3[b]=1;
        parent3[a]=a; 
        union(a,b)
for i in range(N+1): 
    if not invited_M3[i] and invited_M2[i]:
        parent3[i]=i
        invited_M3[i]=0
# print('아')
ans_constant=0
ans=[[i] for i in range(100001)]
print(parent3)


real_ans=[]
arr=[]
for i in range(N+1):
    if parent[i]<i: ans[parent[i]].append(i)
for i in ans:
    if len(i)>=2: real_ans.append(i); ans_constant+=1
print(ans_constant)
for i in real_ans: print(*i)