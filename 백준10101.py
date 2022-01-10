x=int(input())
y=int(input())
z=int(input())

if x+y+z == 180:
    if x==60 and y==60 and z==60:
        print('Equilateral')
    elif x==y or y==z or z==x:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')