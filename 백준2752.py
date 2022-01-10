a,b,c=map(int, input().split())

if a!=min(a,b,c) and a!=max(a,b,c):
    middle=a
elif b!=min(a,b,c) and b!=max(a,b,c):
    middle = b
else:
    middle = c

print(min(a,b,c), middle, max(a,b,c))