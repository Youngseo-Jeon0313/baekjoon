import sys
input=sys.stdin.readline
N=int(input())
#dictionary안에 list
Dict={}
arr=[]
for _ in range(N):
    name,place,start,end=input().split()
    if name in arr: continue
    arr.append(name)
    start=int(start); end=int(end)
    if place in Dict.keys(): 
        for i in range(start,end):
            Dict[place][i]+=1
    else:
        Dict[place]=[0 for _ in range(50001)]
        for i in range(start,end):
            Dict[place][i]+=1

    MAX_index=0; MAX_value=0
for key, value in Dict.items():
    # print(key,value[:10])
    if max(value)>MAX_value: MAX_value=max(value); MAX_index=key
    if max(value)==MAX_value and MAX_index>key: MAX_index=key
# print(MAX_index)
x=Dict[MAX_index]
flag=False

for i in range(50001):
    if x[i]==MAX_value and not flag: print(MAX_index, i, end=' '); flag=True
    if flag and x[i]!=MAX_value: print(i); exit();