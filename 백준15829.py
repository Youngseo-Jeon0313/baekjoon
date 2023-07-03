N=int(input())
S=input()
List=[]
for i in S:
    List.append(ord(i)-ord('a')+1)
ans=0
for i in range(N):
    ans+=(List[i]*(31**(i)) % 1234567891)
print(ans)