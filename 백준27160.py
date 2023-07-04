N=int(input())
dict={}
for i in range(N):
    a,b=input().split()
    if a in dict.keys():
        dict[a]+=int(b)
    else:
        dict[a]=int(b)
flag=True
# print(dict)
for key, value in dict.items():
    if value==5: print('YES'); flag=False; break
if flag: print("NO")
