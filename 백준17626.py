import sys
input=sys.stdin.readline
n=int(input())
'''
딱 떨어지게 해야 함 ..!!

'''
sum=0
for i in range(224,0,-1):
    if i**2<=n and n>0:
        n=n-i**2
        sum+=1
    print(i,n)

sys.stdout.write(str(sum)+'\n')