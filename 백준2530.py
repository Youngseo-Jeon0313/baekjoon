a, b, c = map(int,input().split())
d = int(input())

s = (c+d) % 60
m1 = (c+d) // 60

m = (b+m1) % 60
h1= (b+m1) // 60

h =(h1+a) %24

print(h, m, s)