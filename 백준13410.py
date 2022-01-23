n, k = map(int,input().split())
List=[]
for i in range(1,k+1):
    a=n*i
    a=str(a)
    a=a[::-1]
    List.append(int(a))

print(max(List))
