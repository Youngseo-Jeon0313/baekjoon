R,C,N=map(int,input().split())
a=R//N+bool(R%N)
b=C//N+bool(C%N)
print(a*b)