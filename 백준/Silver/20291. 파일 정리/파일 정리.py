dict={}

N=int(input())
for _ in range(N):
    S=input()
    a,b=S.split(".")
    if b in dict.keys():
        dict[b]+=1
    else:
        dict[b]=1

dict=sorted(dict.items())
for i in dict:
    print(i[0], i[1])