'''
[2,5,1,4,3]


[3,1,4,3,2]
[1,2,3,3,4] -> [1,2,6,9,13] sum(prefix)
'''

N=int(input())
List=list(map(int,input().split()))
List=sorted(List)
for i in range(1,N):
    List[i]+=List[i-1]
print(sum(List))