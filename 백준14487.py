N=int(input())
List=list(map(int,input().split()))
List=sorted(List)
print(sum(List)-List[-1])