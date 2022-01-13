M=list(map(int, input().split()))
a=0
for i in range(len(M)-1):
    if M[i+1]<M[i] :
        a+=1
if a>0:
    print('Bad')
else:
    print("Good")