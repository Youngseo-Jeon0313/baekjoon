STR=input()


a = [True]*(10000+2)


primes=[]

for i in range(2,10000+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i,10000+1, i):
        a[j] = False

ans=0
for i in STR:
    if 65<=ord(i) and ord(i)<97: #대문자
        ans+=ord(i)-ord('A')+27
    else:
        ans+=ord(i)-ord('a')+1
# print(ans)
if a[ans]: print('It is a prime word.')
else: print('It is not a prime word.')