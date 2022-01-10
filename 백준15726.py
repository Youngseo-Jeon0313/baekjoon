A,B,C=map(int, input().split())

a=A*B/C
b=A/B*C

print(int(max(a,b)))