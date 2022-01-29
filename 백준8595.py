n=int(input())
s=input()
s+='a'
List=[]
sum=0
for i in range(n+1):
    if s[i].isdecimal():
        List.append(s[i])
    else:
        if len(List)>0 :
            sum+=int(''.join(map(str,List)))
            List=[]
print(sum)