


n=int(input())
M=list(input())
List=[]

for i in range(n):
    Mist=[]
    for j in range(6):
        Mist.append(M[6*i+j])
    List.append(Mist)


print(List)