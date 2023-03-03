def find(a):
    global parent
    if a==parent[a]: return a
    parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    global parent
    a=find(a)
    b=find(b)
    if a<b: parent[b]=a
    else: parent[a]=b
    
def solution(n, costs):
    global parent
    parent=[i for i in range(n)]
    costs=sorted(costs, key=lambda x:x[2])
    answer = 0
    for a,b,c in costs:
        if find(a)!=find(b): 
            union(a,b);
            answer+=c   
    
    return answer