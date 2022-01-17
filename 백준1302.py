'''
생각!
딕셔너리에 없으면, 넣고 있으면 하나 값 올리고

items를 쓰면 key,value값을 각각 꺼낼 수 있음을 알자!

'''
t=int(input())

Book={}

for i in range(t):
    a=input()
    if a in list(Book.keys()):
        Book[a]+=1
        
    else:
        Book[a]=1

K=Book.keys()
V=Book.values()
M=max(V)


Ans=list()
for key, value in Book.items():
    if value==M:
        Ans.append(key)

Ans=list(set(Ans))
Ans.sort()
print(Ans[0])