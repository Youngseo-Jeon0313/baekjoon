S1,S2=map(int,input().split())
arr=[list(list(map(int,input().split())) )for _ in range(S1)]
for i in arr:
    if i[0]!=i[1]: print('Wrong Answer'); exit()
arr2=[list(list(map(int,input().split())) )for _ in range(S2)]
for j in arr2:
    if j[0]!=j[1]: print("Why Wrong!!!"); exit()
print('Accepted')