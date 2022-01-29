import sys

arr=[]
for line in sys.stdin:
    arr.append(line)
for i in arr:
    UP=0
    DOWN=0
    NUM=0
    SPACE=0
    i=str(i)
    for line in i:
        if line==' ':
            SPACE+=1
        elif line.isdecimal():
            NUM+=1
        elif line==line.upper():
            UP+=1
        elif line==line.lower():
            DOWN+=1
    print(DOWN, UP-1, NUM, SPACE)

